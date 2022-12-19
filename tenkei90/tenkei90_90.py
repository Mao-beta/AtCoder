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


def task1(N, K):
    # N <= 10**5, K == 1
    # aは0/1 a==1が隣り合わなければOK
    # dp[i][j]: i個まで見て直前がj
    dp = [[0]*2 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(2):
            for nj in range(2):
                if j == nj == 1:
                    continue
                dp[i+1][nj] += dp[i][j]
                dp[i+1][nj] %= MOD99

    print(sum(dp[-1]) % MOD99)


# 正方行列の積 mod
def mul_matrix(A, B, mod=10**9+7):
    size = len(A)
    ans = [[0] * size for _ in range(size)]
    for h in range(size):
        for w in range(size):
            for i in range(size):
                ans[h][w] += A[h][i] * B[i][w] % mod
                ans[h][w] %= mod
    return ans

# 正方行列の累乗 mod
def pow_matrix(A, n, mod=10**9+7):
    if n == 1:
        size = len(A)
        E = [[0] * size for _ in range(size)]
        for i in range(size):
            E[i][i] = 1
        return mul_matrix(A, E, mod)

    if n % 2 == 0:
        tA = pow_matrix(A, n//2, mod)
        return mul_matrix(tA, tA, mod)
    else:
        tA = pow_matrix(A, n-1, mod)
        return mul_matrix(tA, A, mod)


def task12(N, K):
    # K==1のときは結局フィボナッチ
    # 行列累乗する
    A = [[1, 1],
         [1, 0]]

    AN = pow_matrix(A, N, MOD99)
    print((AN[0][0] + AN[1][0]) % MOD99)


def task3(N, K):
    # N <= 6, K <= 6
    # (K+1)**N通りを全探索

    def check(A):
        for l in range(N):
            for r in range(l+1, N+1):
                if min(A[l:r]) * (r-l) > K:
                    return False
        return True

    ans = 0
    for P in product(range(K+1), repeat=N):
        ans += int(check(P))

    print(ans % MOD99)


if __name__ == "__main__":
    N, K = NMI()
    if K == 1:
        task12(N, K)
    elif N <= 6 and K <= 6:
        task3(N, K)
    else:
        print(0)