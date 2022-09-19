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
    INF = 10**10
    A = [INF] * 2 + NLI()
    B = [INF] * 3 + NLI()
    dp = [INF] * (N+1)
    dp[1] = 0
    for i in range(2, N+1):
        dp[i] = min(dp[i], dp[i-1] + A[i])
        dp[i] = min(dp[i], dp[i-2] + B[i])
    print(dp[-1])


if __name__ == "__main__":
    main()
