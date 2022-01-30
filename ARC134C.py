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


class HugeComb:
    """nCrのnが10**9くらいあるが、rが200くらい"""
    def __init__(self, r_max, mod=10**9+7):
        assert r_max >= 0
        self.r_max = r_max
        self.inv = [1] * (r_max+1)
        self.mod = mod

        for i in range(1, r_max+1):
            a = self.inv[i-1] * pow(i, mod-2, mod)
            self.inv[i] = a

    def P(self, n, r):
        assert r >= 0
        assert n >= r
        res = 1
        for i in range(r):
            res = res * (n-i) % self.mod
        return res

    def C(self, n, r):
        assert r >= 0
        assert n >= r
        assert r <= self.r_max
        return self.P(n, r) * self.inv[r] % self.mod

    def H(self, n, r):
        return self.C(n+r-1, r-1)


def main():
    N, K = NMI()
    A = NLI()
    HC = HugeComb(205, mod=MOD99)

    ans = 1
    rem = sum(A[1:])
    A[0] -= rem + K

    if A[0] < 0:
        print(0)
        exit()

    for a in A:
        ans = ans * HC.H(a, K) % MOD99

    print(ans)


if __name__ == "__main__":
    main()
