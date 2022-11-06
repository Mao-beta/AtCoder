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
    N, M = NMI()
    com = Comb(int(10**7*1.4), MOD99)

    # x^(N-1) * (1+x)^(N-1)
    F = [0] * (M+1)
    for i in range(N):
        if i + N-1 <= M:
            F[i + N-1] = com.C(N-1, i)

    # (1/1-x3)^(N-1)
    G = [0] * (M+1)
    for j in range(M+1):
        if j*3 <= M:
            G[j*3] = com.C(N-2+j, N-2)

    # (1/1-x)^2 をかける
    G = list(accumulate(G, func=lambda x, y: (x+y) % MOD99))
    G = list(accumulate(G, func=lambda x, y: (x+y) % MOD99))

    ans = 0
    for i in range(M+1):
        ans += F[i] * G[M-i] % MOD99
        ans %= MOD99

    print(ans)


if __name__ == "__main__":
    main()
