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
        """
        n個のものから重複を許してr個取り出す
        """
        return self.C(n + r - 1, r)

    def multi(self, L):
        res = self.fac[sum(L)]
        for l in L:
            res = res * self.inv[l] % self.mod
        return res


def main():
    N, K = NMI()
    A = NLI()

    com = Comb(K+1, MOD99)
    inv2 = pow(2, MOD99-2, MOD99)

    # P[x][i]: Ai^x % MOD99
    P = [[1]*N for _ in range(K+1)]
    for x in range(K):
        for i in range(N):
            P[x+1][i] = P[x][i] * A[i] % MOD99

    S = [sum(p) % MOD99 for p in P]
    # S[0] = 1

    for x in range(1, K+1):
        ans = 0
        for r in range(x+1):
            ans += com.C(x, r) * S[r] % MOD99 * S[x-r]
            # print(com.C(x, r), S[r], S[x-r], x, r)
            ans %= MOD99
        ans -= pow(2, x, MOD99) * S[x] % MOD99
        ans = ans * inv2 % MOD99
        print(ans)


if __name__ == "__main__":
    main()
