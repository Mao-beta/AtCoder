import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]

from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n
        self.roots = set(range(n))
        self.group_num = n
        self.ans = 0
        self.color = [-1] * self.n
        self.rcolor = [[0, 0]] * self.n

    def find(self, x):
        # 根ならその番号を返す
        if self.par[x] < 0:
            return x
        else:
            # 親の親は親
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def is_same(self, x, y):
        # 根が同じならTrue
        return self.find(x) == self.find(y)

    def unite(self, _x, _y):
        x = self.find(_x)
        y = self.find(_y)
        if x == y:
            return

        # 木のサイズを比較し、小さいほうから大きいほうへつなぐ
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.group_num -= 1
        self.roots.discard(y)
        assert self.group_num == len(self.roots)

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

    def get_roots(self):
        return self.roots

    def group_count(self):
        return len(self.roots)


def dfs_paint_01_color(start, graph):
    # 二色塗り分け 二部グラフである前提
    from collections import deque
    n = len(graph)
    colors = [-1] * n

    for start in range(n):
        if colors[start] != -1:
            continue
        stack = deque()
        stack.append(start)

        colors[start] = 0

        while stack:
            now = stack.pop()
            c = colors[now]

            for goto in graph[now]:
                if colors[goto] != -1:
                    continue
                stack.append(goto)
                colors[goto] = 1 - c

    return colors


def adjlist(n, edges, directed=False, in_origin=1) -> list[list[int]]:
    if len(edges) == 0:
        return [[] for _ in range(n)]

    weighted = True if len(edges[0]) > 2 else False
    if in_origin == 1:
        if weighted:
            edges = [[x-1, y-1, w] for x, y, w in edges]
        else:
            edges = [[x-1, y-1] for x, y in edges]

    res = [[] for _ in range(n)]

    if weighted:
        for u, v, c in edges:
            res[u].append([v, c])
            if not directed:
                res[v].append([u, c])

    else:
        for u, v in edges:
            res[u].append(v)
            if not directed:
                res[v].append(u)

    return res


def main():
    N, Q = NMI()
    UV = EI(Q)
    G = adjlist(N, UV)
    UV = [[x-1, y-1] for x, y in UV]
    BPedges = []
    uf = UnionFind(N)
    for u, v in UV:
        if uf.is_same(u, v):
            continue
        else:
            uf.unite(u, v)
            BPedges.append([u, v])
    BP = adjlist(N, BPedges, in_origin=0)
    # print(BPedges, BP)
    colors = dfs_paint_01_color(0, BP)
    # print(colors)

    ans = 0
    nuf = UnionFind(N)
    R2C = [[0, 0] for _ in range(N)]
    for u, c in enumerate(colors):
        R2C[u][c] = 1
    # print(R2C)
    out = False
    for qi, (u, v) in enumerate(UV):
        if out:
            print(-1)
            continue

        if nuf.is_same(u, v):
            if colors[u] == colors[v]:
                print(-1)
                out = True
                continue
            else:
                print(ans)
                continue

        ru, rv = nuf.find(u), nuf.find(v)
        ans -= min(R2C[ru]) + min(R2C[rv])
        nuf.unite(u, v)
        nr = nuf.find(u)
        R2C[nr] = [R2C[ru][0] + R2C[rv][0], R2C[ru][1] + R2C[rv][1]]
        # print(R2C[nr])
        ans += min(R2C[nr])
        # print(R2C)
        print(ans)


if __name__ == "__main__":
    main()
