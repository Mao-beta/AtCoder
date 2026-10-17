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
    N = NI()
    S = SI()
    T = SI()

    INF = 1000
    # dp[l][r]: [l, r)から最大何回消せるか
    dp = [[0]*(N+1) for _ in range(N+1)]

    for r in range(N+1):
        for l in range(r, -1, -1):
            if r - l <= 2:
                dp[l][r] = 0
                continue

            res = max(dp[l+1][r], dp[l][r-1])
            for m in range(l+1, r):
                res = max(res, dp[l][m] + dp[m][r])

            if S[l] == T[0] and S[r-1] == T[2]:
                for m in range(l+1, r-1):
                    if S[m] != T[1]:
                        continue
                    if dp[l+1][m] * 3 == m-(l+1) and dp[m+1][r-1] * 3 == r-1-(m+1):
                        res = max(res, dp[l+1][m] + dp[m+1][r-1] + 1)

            dp[l][r] = res
            # print(l, r, res)

    print(dp[0][N])


if __name__ == "__main__":
    main()
