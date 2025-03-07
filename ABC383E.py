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
    N, M, K = NMI()
    UVW = EI(M)
    UVW.sort(key=lambda x: x[-1])
    UVW = [[x-1, y-1, w] for x, y, w in UVW]
    A = NLI()
    B = NLI()
    A = [x-1 for x in A]
    B = [x-1 for x in B]
    R2A = [0] * N
    R2B = [0] * N
    for a in A:
        R2A[a] += 1
    for b in B:
        R2B[b] += 1

    ans = 0
    uf = UnionFind(N)
    for u, v, w in UVW:
        if uf.is_same(u, v):
            continue
        ru, rv = uf.find(u), uf.find(v)
        ua, ub = R2A[ru], R2B[ru]
        va, vb = R2A[rv], R2B[rv]
        uf.unite(u, v)
        r = uf.find(u)
        if ua > 0 and va > 0:
            R2A[r] = ua + va
        elif ub > 0 and vb > 0:
            R2B[r] = ub + vb
        elif ua > 0 and vb > 0:
            if ua == vb:
                ans += ua * w
                R2A[r] = 0
                R2B[r] = 0
            elif ua > vb:
                ans += vb * w
                R2A[r] = ua - vb
                R2B[r] = 0
            else:
                ans += ua * w
                R2A[r] = 0
                R2B[r] = vb - ua
        elif ub > 0 and va > 0:
            if ub == va:
                ans += ub * w
                R2A[r] = 0
                R2B[r] = 0
            elif ub > va:
                ans += va * w
                R2B[r] = ub - va
                R2A[r] = 0
            else:
                ans += ub * w
                R2B[r] = 0
                R2A[r] = va - ub
        elif ua > 0 or ub > 0:
            R2A[r] = ua
            R2B[r] = ub
        elif va > 0 or vb > 0:
            R2A[r] = va
            R2B[r] = vb

    print(ans)


if __name__ == "__main__":
    main()
