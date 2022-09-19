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
    PA = [NLI() for _ in range(N)]
    PA = [[x-1, y] for x, y in PA]

    # dp[l][r] [l, r)から始めたときの最大値
    # ans: dp[0][N]
    dp = [[0]*(N+1) for _ in range(N+1)]
    for g in range(1, N+1):
        for l in range(0, N+1-g):
            r = l + g
            # lをとる l <= P[l] < rなら加点
            p, a = PA[l]
            dp[l][r] = max(dp[l][r], dp[l+1][r] + a * (l <= p < r))
            # rをとる l <= P[r-1] < rなら加点
            p, a = PA[r-1]
            dp[l][r] = max(dp[l][r], dp[l][r-1] + a * (l <= p < r))

    print(dp[0][N])


if __name__ == "__main__":
    main()
