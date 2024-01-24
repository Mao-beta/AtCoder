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
    N = NI()
    A = [list(map(int, list(SI()))) for _ in range(N)]
    B = [x[:] for x in A]
    for h in range(N):
        for w in range(N):
            if h == 0 and w > 0:
                B[h][w] = A[h][w-1]
            if h == N-1 and w < N-1:
                B[h][w] = A[h][w+1]
            if h > 0 and w == N-1:
                B[h][w] = A[h-1][w]
            if h < N-1 and w == 0:
                B[h][w] = A[h+1][w]
    for row in B:
        print(*row, sep="")



if __name__ == "__main__":
    main()
