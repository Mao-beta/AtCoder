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


class Comb:
    """nCrのnもrも10**7くらいまで"""

    def __init__(self, n, mod):
        self.mod = mod
        self.fac = [1] * (n + 1)
        self.inv = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fac[i] = self.fac[i - 1] * i % self.mod
        self.inv[n] = pow(self.fac[n], self.mod - 2, self.mod)
        for i in range(n - 1, 0, -1):
            self.inv[i] = self.inv[i + 1] * (i + 1) % self.mod

    def C(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self.fac[n] * self.inv[r] % self.mod * self.inv[n - r] % self.mod

    def P(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self.fac[n] * self.inv[n - r] % self.mod

    def H(self, n, r):
        return self.C(n + r - 1, r - 1)


def main():
    N = NI()
    C = Comb(250000, MOD99)
    ans = 0
    for x in range(N**2+1):
        # print(x, C.P(x-1, N-1), C.P(N**2-x, N-1))
        # print(C.C(x-1, N-1) * C.C(N**2-x, N-1) % MOD99 * N**2 % MOD99)
        ans += C.P(x-1, N-1) * C.P(N**2-x, N-1) % MOD99 * N**2 % MOD99 * C.P((N-1)**2, (N-1)**2) % MOD99
        ans %= MOD99
    print((C.P(N**2, N**2) - ans) % MOD99)


if __name__ == "__main__":
    main()