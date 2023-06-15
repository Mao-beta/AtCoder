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
        return self.C(n + r - 1, r)

    def multi(self, L):
        res = self.fac[sum(L)]
        for l in L:
            res = res * self.inv[l] % self.mod
        return res


com = Comb(10000, MOD)


def solveA(N, K):
    return pow(K, N, MOD)


def solveB(N, K):
    return com.P(K, N)


def solveC(N, K):
    # 「玉0個の箱がi個以上」を使って包除原理
    ans = 0
    for i in range(K):
        r = K - i
        ans += (-1)**i * pow(r, N, MOD) * com.C(K, i) % MOD
        ans %= MOD
    return ans


def solveD(N, K):
    return com.C(N+K-1, N)


def solveE(N, K):
    return com.C(K, N)


def solveF(N, K):
    return com.C(N-1, K-1)


def solveG(N, K):
    # ベル数
    # 玉0個の箱の個数を除けば
    # 「玉区別あり 箱区別なし 各1つ以上」(スターリング数)
    # の足し合わせに帰着
    ans = 0
    for i in range(K):
        ans += solveI(N, K-i)
        ans %= MOD
    return ans


def solveH(N, K):
    return 1 if N <= K else 0


def solveI(N, K):
    # スターリング数
    # 「玉区別あり 箱区別あり 各1つ以上」をK!でわる
    ans = solveC(N, K) * com.inv[K] % MOD
    return ans


def solveK(N, K):
    return 1 if N <= K else 0


if __name__ == "__main__":
    N, K = NMI()
    # ans = solveA(N, K)
    # ans = solveB(N, K)
    # ans = solveC(N, K)
    # ans = solveD(N, K)
    # ans = solveE(N, K)
    # ans = solveF(N, K)
    # ans = solveG(N, K)
    # ans = solveH(N, K)
    # ans = solveI(N, K)
    # ans = solveJ(N, K)
    ans = solveK(N, K)
    # ans = solveL(N, K)
    print(ans)
