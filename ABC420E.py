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
    N, Q = NMI()
    uf = UnionFind(N)
    C = [0] * N
    B = [0] * N
    for _ in range(Q):
        q, *X = NMI()

        if q == 1:
            u, v = X[0]-1, X[1]-1
            if uf.is_same(u, v):
                continue
            ru, rv = uf.find(u), uf.find(v)
            bu, bv = B[ru], B[rv]
            uf.unite(u, v)
            r = uf.find(u)
            B[r] = bu + bv

        elif q == 2:
            v = X[0]-1
            if C[v] == 0:
                C[v] = 1
                B[uf.find(v)] += 1
            else:
                C[v] = 0
                B[uf.find(v)] -= 1

        else:
            v = X[0]-1
            if B[uf.find(v)] >= 1:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
