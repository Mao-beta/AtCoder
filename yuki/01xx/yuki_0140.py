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
    N = NI()
    com = Comb(1000, MOD)

    # dp[i][j]: i組の夫婦セットでjグループ作る分け方
    # 新しいペアを i-1,j-1に単独グループで追加 or i-1,jのどこかに追加
    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(1, i+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j] * j
            dp[i][j] %= MOD
    ans = 0
    for p in range(N+1):
        np = N-p
        for g in range(p+1):
            # ペアがp組、グループがg個のとき、残りnp組をgグループに各々分けて入れる
            tmp = dp[p][g] * pow(g * (g-1), np, MOD) % MOD * com.C(N, p) % MOD
            # print(p, np, g, tmp)
            ans += tmp
    print(ans % MOD)


if __name__ == "__main__":
    main()
