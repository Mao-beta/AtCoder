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
    T = NI()
    com = Comb(500, MOD99)

    def free(B, X):
        # B桁自由で残りがX個
        res = 0
        cnt = com.C(B, X)
        if X == 0:
            return res, cnt
        for b in range(B):
            res += (1<<b) * com.C(B-1, X-1)
            res %= MOD99
        return res, cnt

    for _ in range(T):
        N, K = NMI()
        N = bin(N)[2:]
        ans = 0
        over = 0
        L = len(N)
        rem = K
        for i, s in enumerate(N):
            s = int(s)

            if s == 1 and rem >= 0:
                rem -= 1
                res, cnt = free(L-1-i, rem+1)
                ans += res + cnt * over
                ans %= MOD99

                over += s * (1 << (L - 1 - i))

                # print(f"{i=}, {L-1-i=}, {rem+1=}, {res=}, {cnt=}, {over=}, {ans=}")

        if N.count("1") == K:
            ans += int(N, 2)
        print(ans % MOD99)


if __name__ == "__main__":
    main()
