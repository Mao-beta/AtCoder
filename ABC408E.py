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


def main():
    N, M = NMI()
    UVW = EI(M)
    UVW = [[x-1, y-1, w] for x, y, w in UVW]
    ngs = [0] * 32
    for b in range(31, -1, -1):
        uf = UnionFind(N)
        ngs[b] = 1
        for u, v, w in UVW:
            ok = True
            for i in range(32):
                if (w >> i) & 1 and ngs[i]:
                    ok = False
            if ok:
                # print(b, u, v, w)
                uf.unite(u, v)
        if not uf.is_same(0, N-1):
            ngs[b] = 0
    # print(ngs)
    ans = 0
    for b in range(32):
        if ngs[b] == 0:
            ans += 1 << b
    print(ans)



if __name__ == "__main__":
    main()
