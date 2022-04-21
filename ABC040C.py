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
    INF = 10**10
    dp = [INF] * N
    dp[0] = 0
    for i in range(N-1):
        if i < N-1:
            dp[i+1] = min(dp[i+1], dp[i] + abs(A[i+1]-A[i]))
        if i < N-2:
            dp[i+2] = min(dp[i+2], dp[i] + abs(A[i+2]-A[i]))
    print(dp[-1])


if __name__ == "__main__":
    main()
