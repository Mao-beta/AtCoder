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
    N, M = NMI()
    A = [[0] * N for _ in range(N)]
    for _ in range(M):
        k, *X = NMI()
        for x in X:
            for y in X:
                A[x-1][y-1] = 1

    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                print("No")
                exit()

    print("Yes")


if __name__ == "__main__":
    main()
