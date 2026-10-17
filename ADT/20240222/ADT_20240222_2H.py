import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]


def main():
    H, W = NMI()
    S = [SI() for _ in range(H)]
    uf = UnionFind(H*W)
    DH = [0, 1, 0, -1]
    DW = [1, 0, -1, 0]
    red = 0
    for h, s in enumerate(S):
        red += s.count(".")
        for w, ss in enumerate(s):
            if ss == ".":
                continue
            for dh, dw in zip(DH, DW):
                nh, nw = h+dh, w+dw
                if nh < 0 or nh >= H or nw < 0 or nw >= W:
                    continue
                if S[nh][nw] == ".":
                    continue
                uf.unite(h*W+w, nh*W+nw)
    green = uf.group_num - red
    E = 0
    for h, s in enumerate(S):
        for w, ss in enumerate(s):
            if ss == "#":
                continue
            G = set()
            for dh, dw in zip(DH, DW):
                nh, nw = h+dh, w+dw
                if nh < 0 or nh >= H or nw < 0 or nw >= W:
                    continue
                if S[nh][nw] == ".":
                    continue
                G.add(uf.find(nh*W+nw))
            E += green - (len(G)-1)

    print(E * pow(red, -1, MOD99) % MOD99)


if __name__ == "__main__":
    main()
