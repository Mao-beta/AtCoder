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


def force(N):
    R = list(range(1, 2*N+1))

    D = defaultdict(int)

    for P in permutations(R, N):
        S = set(R)
        for p in P:
            S.discard(p)
        P = sorted(list(P))
        S = sorted(list(S))
        m = 0
        print(P, S)
        for p, s in zip(P, S):
            m += p * s
        print(m)

        D[m] += 1

    D = list(D.items())
    D.sort(reverse=True)
    ans = D[0][1]
    for i in range(1, N+1):
        ans *= i * i
    print(N, D[0][1], ans)


class Comb:
    """nCrのnもrも10**7くらいまで"""
    def __init__(self, n, mod):
        self.mod = mod
        self.fac = [1] * (n + 1)
        self.inv = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fac[i] = self.fac[i - 1] * i % self.mod
        self.inv[n] = pow(self.fac[n], self.mod-2, self.mod)
        for i in range(n-1, 0, -1):
            self.inv[i] = self.inv[i+1] * (i+1) % self.mod

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



def main(N):
    if N == 2:
        print(16)
        return

    com = Comb(N*2+10, MOD99)
    print(com.C(2*N, N) * com.P(N, N) % MOD99)


if __name__ == "__main__":
    N = NI()
    main(N)
