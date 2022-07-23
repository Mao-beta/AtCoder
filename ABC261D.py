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
    X = NLI()
    CY = [NLI() for _ in range(M)]
    Bonus = [0] * (N+1)

    for c, y in CY:
        Bonus[c] += y

    # print(Bonus)

    # i回投げてj回連続のときの最大
    dp = [[0]*(N+1) for _ in range(N+1)]

    for i in range(N):
        # print(i, X[i])
        for j in range(i+1):
            # 表
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + X[i] + Bonus[j+1])
            # 裏
            dp[i+1][0] = max(dp[i+1][0], dp[i][j])

        # print(dp[i+1])

    print(max(dp[-1]))


if __name__ == "__main__":
    main()
