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

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

    def get_roots(self):
        return self.roots

    def group_count(self):
        return len(self.roots)



def main():
    N, M = NMI()
    X = NLI()
    Y = NLI()
    ABZ = [NLI() for _ in range(M)]
    X = [[i, N, x] for i, x in enumerate(X)]
    Y = [[i, N+1, x] for i, x in enumerate(Y)]
    ABZ = [[x-1, y-1, w] for x, y, w in ABZ]
    ABZ.sort(key=lambda x: x[2])

    uf = UnionFind(N)
    ans_r = 0
    for a, b, z in ABZ:
        if not uf.is_same(a, b):
            ans_r += z
            uf.unite(a, b)

    if uf.group_num != 1:
        ans_r = 10**20

    uf = UnionFind(N+1)
    ans_a = 0
    E = ABZ + X
    E.sort(key=lambda x: x[2])
    for a, b, z in E:
        if not uf.is_same(a, b):
            ans_a += z
            uf.unite(a, b)

    uf = UnionFind(N + 1)
    ans_p = 0
    E = ABZ + Y
    E.sort(key=lambda x: x[2])
    for a, b, z in E:
        if b == N+1:
            b = N
        if not uf.is_same(a, b):
            ans_p += z
            uf.unite(a, b)

    uf = UnionFind(N+2)
    ans_ap = 0
    E = ABZ + X + Y
    E.sort(key=lambda x: x[2])
    for a, b, z in E:
        if not uf.is_same(a, b):
            ans_ap += z
            uf.unite(a, b)

    print(min(ans_r, ans_p, ans_a, ans_ap))


if __name__ == "__main__":
    main()
