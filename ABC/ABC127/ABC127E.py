import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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


class Comb:
    """nCrのnもrも10**6くらい"""
    def __init__(self, n, mod):
        self.mod = mod
        self.fac = [1] * (n + 1)
        self.inv = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fac[i] = self.fac[i - 1] * i % self.mod
            self.inv[i] = self.inv[i - 1] * pow(i, self.mod - 2, self.mod) % self.mod

    def C(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self.fac[n] * self.inv[r] % self.mod * self.inv[n - r] % self.mod

    def P(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self.fac[n] * self.inv[n - r] % self.mod

    def H(self, n, r):
        return self.C(n+r-1, r-1)


def main():
    N, M, K = NMI()
    com = Comb(2*10**5, MOD)

    tmp = 0
    for d in range(N):
        tmp += d * (N - d) * M ** 2 % MOD
        tmp %= MOD
    for d in range(M):
        tmp += d * (M - d) * N ** 2 % MOD
        tmp %= MOD

    tmp = tmp * com.C(N*M-2, K-2) % MOD
    print(tmp)


if __name__ == "__main__":
    main()
