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
    X, Y, R, N = NMI()
    S = [["." for _ in range(2*N+1)] for _ in range(2*N+1)]
    X += N
    Y += N
    for x in range(2*N+1):
        for y in range(2*N+1):
            if (X-x)**2 + (Y-y)**2 <= R**2:
                S[x][y] = "#"
    for row in S:
        print(" ".join(row))


if __name__ == "__main__":
    main()
