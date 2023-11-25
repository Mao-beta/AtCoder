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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    X, Y, Z = NMI()
    S = SI()
    N = len(S)
    INF = 10**15
    # dp[i][j]: i(off/on)の状態でj文字終えたときの秒数
    dp = [[INF]*(N+1) for _ in range(2)]
    dp[0][0] = 0
    for j, s in enumerate(S):
        for i in range(2):
            d = dp[i][j]
            if d == INF: continue
            if s == "a":
                if i == 0:
                    dp[i][j+1] = min(dp[i][j+1], d+X)
                    dp[i^1][j+1] = min(dp[i^1][j+1], d+Z+Y)
                else:
                    dp[i][j + 1] = min(dp[i][j + 1], d + Y)
                    dp[i ^ 1][j + 1] = min(dp[i ^ 1][j + 1], d + Z + X)

            else:
                if i == 0:
                    dp[i][j+1] = min(dp[i][j+1], d+Y)
                    dp[i^1][j+1] = min(dp[i^1][j+1], d+Z+X)
                else:
                    dp[i][j + 1] = min(dp[i][j + 1], d + X)
                    dp[i ^ 1][j + 1] = min(dp[i ^ 1][j + 1], d + Z + Y)

    ans = min(dp[0][-1], dp[1][-1])
    print(ans)



if __name__ == "__main__":
    main()
