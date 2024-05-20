import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    N, C = NMI()
    A = NLI()
    cum = list(accumulate([0]+A))
    S = cum[-1]
    if C > 0:
        gap = 0
        m = 0
        for c in cum:
            gap = max(gap, c-m)
            m = min(m, c)
        print(gap * (C-1) + S)
    else:
        gap = 0
        M = 0
        for c in cum:
            gap = min(gap, c - M)
            M = max(M, c)
        print(gap * (C - 1) + S)


if __name__ == "__main__":
    main()
