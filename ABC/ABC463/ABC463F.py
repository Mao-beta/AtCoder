import itertools
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
    N = NI()
    K = EI(N)
    Types = [0] * 6
    MT = [0] * 5
    M = max(sum(K, []))
    TL = [[] for _ in range(6)]

    com = Comb(10**6, MOD99)
    inv2 = pow(2, -1, MOD99)

    # print(M)
    for i, (p, q) in enumerate(K):
        l, r = i*2, i*2+1
        if p == q == M:
            Types[0] += 2
            TL[0].append(l)
            TL[0].append(r)
            MT[0] += 1
        elif max(p, q) == M and min(p, q) == M-1:
            Types[1] += 1
            Types[2] += 1
            if p > q:
                TL[1].append(l)
                TL[2].append(r)
            else:
                TL[2].append(l)
                TL[1].append(r)
            MT[1] += 1
        elif max(p, q) == M and min(p, q) < M-1:
            Types[3] += 1
            if p > q:
                TL[3].append(l)
            else:
                TL[3].append(r)
            MT[2] += 1
        elif p == q == M-1:
            Types[4] += 2
            TL[4].append(l)
            TL[4].append(r)
            MT[3] += 1
        elif max(p, q) == M-1:
            Types[5] += 1
            if p > q:
                TL[5].append(l)
            else:
                TL[5].append(r)
            MT[4] += 1
    # print(Types)
    # print(TL)
    ans = [0] * (2*N)

    # T0 常にM+1
    a, b, c = MT[0], MT[1], MT[2]
    if a > 0:
        tmp = 0
        for x in range(b+c+1):
            tmp += pow(inv2, b+c+1, MOD99) * com.C(b+c, x) % MOD99 * pow(a+x, -1, MOD99) % MOD99
            tmp %= MOD99
        for i in TL[0]:
            ans[i] += tmp
            ans[i] %= MOD99

    # T1, T3でM+1
    a, b, c = MT[0], MT[1], MT[2]
    tmp = 0
    for x in range(b+c):
        tmp += pow(inv2, b + c, MOD99) * com.C(b + c-1, x) % MOD99 * pow(a + x+1, -1, MOD99) % MOD99
        tmp %= MOD99
    for i in TL[1]:
        ans[i] += tmp
        ans[i] %= MOD99
    for i in TL[3]:
        ans[i] += tmp
        ans[i] %= MOD99

    if MT[0] > 0:
        print(*ans)
        return

    # T1, T3でM T4は半分
    a, b, c, d, e = MT
    tmp = 0
    for x in range(e+1):
        tmp += pow(inv2, b+c+e, MOD99) * com.C(e, x) % MOD99 * pow(2*b+c+d+x, -1, MOD99) % MOD99
        tmp %= MOD99
    for i in TL[1]:
        ans[i] += tmp
        ans[i] %= MOD99
    for i in TL[2]:
        ans[i] += tmp
        ans[i] %= MOD99
    for i in TL[3]:
        ans[i] += tmp
        ans[i] %= MOD99
    for i in TL[4]:
        ans[i] += tmp * inv2 % MOD99
        ans[i] %= MOD99

    # T5でM
    a, b, c, d, e = MT
    tmp = 0
    for x in range(e + 1):
        tmp += pow(inv2, b + c + e, MOD99) * com.C(e-1, x) % MOD99 * pow(2 * b + c + d + x+1, -1, MOD99) % MOD99
        tmp %= MOD99
    for i in TL[5]:
        ans[i] += tmp
        ans[i] %= MOD99

    print(*ans)


if __name__ == "__main__":
    main()
