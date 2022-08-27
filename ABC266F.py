import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


def adjlist(n, edges, directed=False, in_origin=1):
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


from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n
        self.roots = set(range(n))
        self.group_num = n
        self.members = defaultdict(set)

        for i in range(n):
            self.members[i].add(i)

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

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return

        # 木のサイズを比較し、小さいほうから大きいほうへつなぐ
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.group_num -= 1
        self.roots.discard(y)
        assert self.group_num == len(self.roots)

        self.members[x] |= self.members[y]
        self.members[y] = set()

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

    def get_members(self, x):
        root = self.find(x)
        return self.members[root]

    def get_roots(self):
        return self.roots

    def group_count(self):
        return len(self.roots)

    def all_group_members(self):
        return self.members

    def __repr__(self):
        return '\n'.join('{}: {}'.format(r, self.members[r]) for r in self.roots)


def _find_cycle(N, G, root):
    """
    グラフの閉路を1つ発見する
    :param N: 頂点数
    :param G: 隣接グラフ
    :param root: 始点
    :return: G内の閉路を構成する頂点のlist
    """
    seen = [0] * N
    finished = [0] * N

    hist = deque()
    pos = [-1]

    def rec(now, par):
        seen[now] = 1
        hist.append(now)

        for to in G[now]:
            if to == par: continue

            if finished[to]: continue

            if seen[to] and not finished[to]:
                pos[0] = to
                return

            rec(to, now)

            if pos[0] != -1:
                return

        hist.pop()
        finished[now] = 1

    rec(root, -1)

    cycle = []
    while hist:
        t = hist.pop()
        cycle.append(t)
        if t == pos[0]:
            break

    return cycle


def find_cycle(N, G, root):
    """
    単純無向グラフの閉路を1つ発見する(非再帰)
    bfsでrootから探索し、parとdepthを保持
    探索済みの点にぶつかったら2点からroot方向へ戻る
    depthの深いほうを先に戻し、あとは同時に戻って同じ点に行けば終わり

    :param N: 頂点数
    :param G: 隣接グラフ
    :param root: 始点
    :return: G内の閉路を構成する頂点のlist
    """
    pars = [N] * N
    depth = [-1] * N
    depth[root] = 0

    que = deque()
    que.append(root)

    u = -1
    v = -1

    # bfs
    while que:
        now = que.popleft()

        for to in G[now]:
            if to == pars[now]: continue
            if depth[to] != -1:
                u = now
                v = to
                break

            depth[to] = depth[now] + 1
            pars[to] = now
            que.append(to)

        if u != -1 and v != -1:
            break

    # のぼる
    du, dv = depth[u], depth[v]
    if du < dv:
        u, v = v, u
        du, dv = dv, du

    U = []
    V = []

    while du > dv:
        U.append(u)
        u = pars[u]
        du -= 1

    while True:
        U.append(u)
        u = pars[u]
        V.append(v)
        v = pars[v]
        if u == v:
            U.append(u)
            break

    cycle = U + V[::-1]

    return cycle


def main():
    N = NI()
    UV = [NLI() for _ in range(N)]
    UV = [[x-1, y-1] for x, y in UV]
    Q = NI()
    XY = [NLI() for _ in range(Q)]
    XY = [[x-1, y-1] for x, y in XY]

    G = adjlist(N, UV, in_origin=0)

    cycle = find_cycle(N, G, 0)
    cycle = set(cycle)

    uf = UnionFind(N)
    pars = [N] * N

    for root in cycle:
        # bfs
        que = deque()
        que.append(root)

        while que:
            now = que.popleft()

            for to in G[now]:
                if to == pars[now]: continue
                if to in cycle:
                    continue
                pars[to] = now
                uf.unite(now, to)
                que.append(to)

    for x, y in XY:
        if uf.is_same(x, y):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
