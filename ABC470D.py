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
    P = NLI()
    P = [x-1 for x in P]
    R = [0] * N
    for i, p in enumerate(P):
        R[p] = i
    rev = False
    for _ in range(Q):
        q, *xy = NMI()
        if q == 1:
            x, y = xy
            x, y = x-1, y-1
            if rev:
                P[R[x]], P[R[y]] = P[R[y]], P[R[x]]
                R[x], R[y] = R[y], R[x]
            else:
                R[P[x]], R[P[y]] = R[P[y]], R[P[x]]
                P[x], P[y] = P[y], P[x]
        else:
            rev = not rev
    if rev:
        print(*[r+1 for r in R])
    else:
        print(*[p+1 for p in P])



if __name__ == "__main__":
    main()
