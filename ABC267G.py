import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, groupby

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

    def multi(self, L):
        res = self.fac[sum(L)]
        for l in L:
            res = res * self.inv[l] % self.mod
        return res


def main():
    N, K = NMI()
    A = NLI()
    A.sort()
    AL = [x for a, x in sorted(Counter(A).items())]
    # print(AL)

    com = Comb(N+5, MOD99)

    # dp[n][m] n個まで決めてm個条件を満たす場合の数
    dp = [0] * (6000*6000)
    dp[0*6000+0] = 1
    # dp = [[0]*(K+1) for _ in range(N+1)]
    # dp[0][0] = 1

    n = 0
    for x in AL:
        nn = n + x
        base = com.P(x, x)
        for m in range(min(n+1, K+1)):
            res = base * dp[n*6000+m]
            res %= MOD99
            if dp[n*6000+m] == 0: continue
            for k in range(x+1):
                nm = m + k
                if nm > K: break

                dp[nn*6000+nm] += res * com.C(n-m, k) % MOD99 * com.C(x+m, x-k) % MOD99
                dp[nn*6000+nm] %= MOD99

        n = nn

    print(dp[N*6000+K])



if __name__ == "__main__":
    main()
