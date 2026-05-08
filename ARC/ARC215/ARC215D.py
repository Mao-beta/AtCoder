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
        """
        n個のものから重複を許してr個取り出す
        """
        if n == r == 0:
            return 1
        return self.C(n + r - 1, r)

    def multi(self, L):
        res = self.fac[sum(L)]
        for l in L:
            res = res * self.inv[l] % self.mod
        return res


def main():
    N, M = NMI()
    com = Comb(10**7*2+5, MOD)
    Ne = (N+1) // 2
    No = N - Ne
    Go = [0] * (M+1)
    Bgo = [0] * (M+1)
    for g in range(M+1):
        # A0=0, A_-1 = g
        k = com.C(g+No-2, g)
        Bgo[g] = k
        Go[g] = k * (M-g+1) % MOD
    CGo = list(accumulate([0] + Go))
    CBGo = list(accumulate([0] + Bgo))
    ans = 0
    for ge in range(M+1):
        k = com.C(ge + Ne - 2, ge)
        km = k * (M-ge+1) % MOD
        ans += k * (CGo[ge] - CGo[0]) % MOD
        ans += km * (CBGo[M+1] - CBGo[ge]) % MOD
        ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
