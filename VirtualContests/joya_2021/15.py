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
NLLI = lambda n: [NLI() for _ in range(n)]
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


def main():
    N = NI()
    T = NLI()
    M = NI()
    PX = NLLI(M)
    base = sum(T)
    for p, x in PX:
        p -= 1
        print(base - T[p] + x)


if __name__ == "__main__":
    main()
