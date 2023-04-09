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


def main():
    H, W, K = NMI()
    com = Comb(10**6+5, MOD99)

    ans = 0

    for h in range(1, H+1):
        for w in range(1, W+1):
            if h*w < K:
                continue

            # K個がとある h*w の長方形にちょうどおさまる
            c = com.C(h*w, K)\
                - com.C((h-1)*w, K) * 2 - com.C(h*(w-1), K) * 2\
                + com.C((h-2)*w, K) + com.C(h*(w-2), K) + com.C((h-1)*(w-1), K) * 4\
                - com.C((h-2)*(w-1), K) * 2 - com.C((h-1)*(w-2), K) * 2 \
                + com.C((h-2)*(w-2), K) * (h >= 2 or w >= 2) # h=w=1 のとき (h-2)*(w-2)=1になってしまう

            # 長方形のとりかた (H-h+1) * (W-w+1)
            # スコア h * w
            c *= (H-h+1) * (W-w+1) * h * w % MOD99
            c %= MOD99
            ans += c
            ans %= MOD99

    # HW_C_K通りでわる
    ans *= pow(com.C(H*W, K), MOD99-2, MOD99)
    ans %= MOD99
    print(ans)


if __name__ == "__main__":
    main()
