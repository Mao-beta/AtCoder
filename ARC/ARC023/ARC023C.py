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


from typing import List
from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> "List[tuple[str, int]]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


def main():
    N = NI()
    A = NLI()
    C = HugeComb(2500, MOD)
    A = runLengthEncode(A)
    ans = 1
    for i, (a, k) in enumerate(A):
        if a != -1: continue
        x = A[i+1][0] - A[i-1][0]
        ans = ans * C.C(x+k, k) % MOD
    print(ans)


if __name__ == "__main__":
    main()
