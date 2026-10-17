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
EI = lambda m: [NLI() for _ in range(m)]


class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n
        self.roots = set(range(n))

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

        self.roots.discard(y)

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

    def f(a, b):
        return a * (N + 1) + b

    def g(x):
        return divmod(x, N + 1)

    AB = set()
    for _ in range(M):
        a, b = NMI()
        AB.add(f(a, b))

    Q = NI()
    TXY = EI(Q)

    UF = []
    for t, x, y in TXY:
        if t == 1:
            uf = UnionFind(N+1)
            for ab in AB:
                a, b = g(ab)
                uf.unite(a, b)
            UF.append(uf)
            AB.add(f(x, y))
        if t == 2:
            AB.discard(f(x, y))

    uf = UnionFind(N + 1)
    for ab in AB:
        a, b = g(ab)
        # print(a, b)
        uf.unite(a, b)
    UF.append(uf)

    ans = []
    idx = len(UF) - 1
    for t, x, y in TXY[::-1]:
        if t == 1:
            idx -= 1
        elif t == 2:
            UF[idx].unite(x, y)
        else:
            ans.append(UF[idx].is_same(x, y))
    
    for x in ans[::-1]:
        if x:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
