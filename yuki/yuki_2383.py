import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    N, K = NMI()
    if N == 1:
        print([0, 1, 3, 3, 3, 1, 1][K])
        return

    com = Comb(N*10, MOD99)
    ans = com.C(2*N+4, K)
    if N % 2:
        if K % 2 == 0:
            ans += com.C(N+2, K//2) * 2 # 上下反転・上下左右反転
        # 左右反転はKの偶奇でかわる
        if K % 2 == 0:
            # 中心が0個
            ans += com.C(N+1, K//2)
            # 中心が2個
            ans += com.C(N+1, (K-2)//2)
        else:
            # 中心が1個
            ans += com.C(N+1, (K-1)//2) * 2
    else:
        if K % 2 == 0:
            ans += com.C(N+2, K//2) * 3
    ans = ans * pow(4, MOD99-2, MOD99) % MOD99
    print(ans)


if __name__ == "__main__":
    main()
