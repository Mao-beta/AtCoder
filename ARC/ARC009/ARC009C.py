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


class HugeComb:
    """nCrのnが10**9くらいあるが、rが10**5くらい"""
    def __init__(self, r_max, mod=10**9+7):
        assert r_max >= 0
        self.r_max = r_max
        self.inv = [1] * (r_max+1)
        self.mod = mod

        for i in range(1, r_max+1):
            a = self.inv[i-1] * pow(i, mod-2, mod) % mod
            self.inv[i] = a

    def P(self, n, r):
        assert r >= 0
        assert n >= r
        res = 1
        for i in range(r):
            res = res * (n-i) % self.mod
        return res

    def C(self, n, r):
        assert r <= self.r_max
        return self.P(n, r) * self.inv[r] % self.mod

    def H(self, n, r):
        return self.C(n+r-1, r-1)


def main():
    N, K = NMI()
    MOD = 1_777_777_777
    com = HugeComb(K+1, MOD)
    F = [0, 0, 1, 2] # 攪乱順列の個数
    for i in range(4, K+1):
        F.append((i-1) * (F[-1]+F[-2]) % MOD)
    print(com.C(N, K) * F[K] % MOD)


if __name__ == "__main__":
    main()
