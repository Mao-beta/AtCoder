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
    TD = [NLI() for _ in range(N)]
    TD.sort(key=lambda x: x[1])

    DM = 1440
    dp = [[-1000]*(DM+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        t, d = TD[i]
        for j in range(DM+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j+t <= d:
                dp[i+1][j+t] = max(dp[i+1][j+t], dp[i][j]+1)

    print(max(dp[-1]))


if __name__ == "__main__":
    main()
