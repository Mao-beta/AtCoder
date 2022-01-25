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
    C = NLI()
    INF = 10**10
    dp = [INF] * (N+10005)
    dp[0] = 0
    for i in range(N+1):
        for c in C:
            dp[i+c] = min(dp[i+c], dp[i]+1)
    print(dp[N])


if __name__ == "__main__":
    main()
