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
    N = NI()
    A = NLI()
    Q = NI()
    M = NLI()
    dp = [[0]*40001 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        a = A[i]
        for j in range(40001):
            if dp[i][j] == 0: continue
            dp[i+1][j] = 1
            if j+a <= 40000:
                dp[i+1][j+a] = 1

    for m in M:
        print("yes" if dp[-1][m] else "no")


if __name__ == "__main__":
    main()
