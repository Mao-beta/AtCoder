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
    W = [NI() for _ in range(N)]

    Com = Comb(100, MOD99)

    # n種類について処理した m種類取った k回引いた　ときの場合の数
    dp = [[[0]*(K+1) for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1

    for n in range(N):
        for m in range(M+1):
            for k in range(K+1):
                if dp[n][m][k] == 0: continue

                # 1個も引かない
                dp[n+1][m][k] += dp[n][m][k]
                dp[n+1][m][k] %= MOD99

                # これ以上引けない場合
                if m == M or k == K: continue

                # c個引くのを全探索
                for c in range(1, K-k+1):
                    # 1種類増えて、c回引いたとき、 wi^c / c! をかける
                    # Σci = Kに注意すると、重複を考慮すれば
                    # 最終的に (w1^c1 * w2^c2 * ...) * K! / (c1! * c2! * ...) になるが、K!は最後にかける
                    dp[n+1][m+1][k+c] += dp[n][m][k] * pow(W[n], c, MOD99) * Com.inv[c]
                    dp[n+1][m+1][k+c] %= MOD99

    # dp[N][M][K] * K! / (sumW)^K
    # sumW^Kで割ることで場合の数を確率にする
    print(dp[N][M][K] * pow(sum(W), (MOD99-2)*K, MOD99) % MOD99 * Com.fac[K] % MOD99)


if __name__ == "__main__":
    main()
