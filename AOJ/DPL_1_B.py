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
    N, W = NMI()
    VW = [NLI() for _ in range(N)]
    dp = [[0]*(W+1) for _ in range(N+1)]
    for i in range(N):
        v, w = VW[i]
        for j in range(W):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j+w <= W:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j+w] + v)
    print(max(dp[N]))


if __name__ == "__main__":
    main()
