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


def main():
    H, W = NMI()
    G = [SI() for _ in range(H)]
    uf = UnionFind(H*W)

    def f(h, w):
        return h * W + w

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    for now_h in range(H):
        for now_w in range(W):
            if G[now_h][now_w] == "#":
                continue

            i = f(now_h, now_w)

            for dh, dw in zip(DH, DW):
                goto_h = now_h + dh
                goto_w = now_w + dw

                if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                    continue
                if G[goto_h][goto_w] == "#":
                    continue

                gi = f(goto_h, goto_w)
                uf.unite(i, gi)

    R = set()
    for now_h in range(H):
        for now_w in range(W):
            if G[now_h][now_w] == "#":
                continue

            i = f(now_h, now_w)
            R.add(uf.find(i))


    ans = 0
    for now_h in range(H):
        for now_w in range(W):
            if G[now_h][now_w] == ".":
                continue

            adj = set()
            for dh, dw in zip(DH, DW):
                goto_h = now_h + dh
                goto_w = now_w + dw

                if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                    continue
                if G[goto_h][goto_w] == ".":
                    adj.add(uf.find(f(goto_h, goto_w)))

            if len(adj) == len(R):
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()