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


def main():
    N = NI()
    A = SI()

    def rec(l, r):
        Z2O = []
        O2Z = []
        S = []
        g = r-l
        if g == 1:
            s = int(A[l])
            if s == 0:
                return 1, 0, 0
            else:
                return 0, 1, 1

        for i in range(3):
            z2o, o2z, s = rec(l+g//3*i, l+g//3*(i+1))
            Z2O.append(z2o)
            O2Z.append(o2z)
            S.append(s)

        if S.count(0) <= 1:
            ns = 1
        else:
            ns = 0
        if ns == 0:
            no2z = 0
            Z2O.sort()
            nz2o = Z2O[0] + Z2O[1]
            return nz2o, no2z, ns
        else:
            nz2o = 0
            O2Z.sort()
            no2z = O2Z[0] + O2Z[1]
            return nz2o, no2z, ns

    z2o, o2z, s = rec(0, 3**N)
    print(max(z2o, o2z))


if __name__ == "__main__":
    main()
