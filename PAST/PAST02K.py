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
    S = SI()
    C = NLI()
    D = NLI()
    INF = 10**20
    # i個まで見て"("がj個余っているときのコスト
    dp = [[INF]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        s = S[i]
        for j in range(N+1):
            if dp[i][j] >= INF: continue
            if s == "(":
                # (
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j])
                # )
                if j > 0:
                    dp[i+1][j-1] = min(dp[i+1][j-1], dp[i][j]+C[i])
                # del
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+D[i])
            else:
                # (
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+C[i])
                # )
                if j > 0:
                    dp[i+1][j-1] = min(dp[i+1][j-1], dp[i][j])
                # del
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+D[i])

    print(dp[-1][0])


if __name__ == "__main__":
    main()
