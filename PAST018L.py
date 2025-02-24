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
    SP = [SMI() for _ in range(N)]
    INF = 10**10
    m = -INF
    M = INF
    neg = False
    for s, p in SP:
        p = int(p)
        if s == "NEGATE":
            neg = not neg
            m, M = -M, -m
        elif s == "CHMIN":
            M = min(M, p)
            m = min(m, M)
        else:
            m = max(m, p)
            M = max(M, m)
    for _ in range(Q):
        q = NI()
        if neg:
            q = -q
        if q < m:
            print(m)
        elif m <= q <= M:
            print(q)
        else:
            print(M)


if __name__ == "__main__":
    main()
