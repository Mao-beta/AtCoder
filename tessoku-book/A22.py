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
    A = [0] + NLI()
    B = [0] + NLI()
    INF = 10**10
    dp = [-INF] * (N+1)
    dp[1] = 0
    for i in range(1, N):
        a, b = A[i], B[i]
        dp[a] = max(dp[a], dp[i] + 100)
        dp[b] = max(dp[b], dp[i] + 150)

    print(dp[N])


if __name__ == "__main__":
    main()
