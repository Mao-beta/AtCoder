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
    N, Q = NMI()
    P2N = [i for i in range(N)]
    N2L = [i for i in range(N)]
    L2N = [i for i in range(N)]
    N2Ps = [{i} for i in range(N)]
    for _ in range(Q):
        q, *X = NMI()
        if q == 1:
            a, b = X
            a -= 1
            b -= 1
            b = L2N[b]
            an = P2N[a]
            N2Ps[an].discard(a)
            N2Ps[b].add(a)
            P2N[a] = b
        elif q == 2:
            a, b = X
            a -= 1
            b -= 1
            na, nb = L2N[a], L2N[b]
            L2N[a], L2N[b] = nb, na
            N2L[na], N2L[nb] = b, a
        else:
            a = X[0]-1
            print(N2L[P2N[a]] + 1)


if __name__ == "__main__":
    main()
