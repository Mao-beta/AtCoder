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


def main():
    N, X, Y = NMI()
    R = [0] * 11
    B = [0] * 11
    R[N] = 1

    for n in range(N, 1, -1):
        r = R[n]
        R[n-1] += r
        B[n] += r * X

        b = B[n]
        R[n-1] += b
        B[n-1] += b * Y

    print(B[1])


if __name__ == "__main__":
    main()
