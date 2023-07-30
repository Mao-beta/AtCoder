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
    S = SI()
    N = len(S)
    # i個みて、それ以前に余っている(がj個
    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        s = S[i]
        for j in range(N):
            d = dp[i][j]

            if s == "(":
                dp[i+1][j+1] += d
                dp[i+1][j+1] %= MOD99
            elif s == ")":
                if j == 0:
                    continue
                dp[i+1][j-1] += d
                dp[i+1][j-1] %= MOD99
            else:
                dp[i+1][j+1] += d
                dp[i+1][j+1] %= MOD99
                if j > 0:
                    dp[i+1][j-1] += d
                    dp[i+1][j-1] %= MOD99

    # print(*dp, sep="\n")
    print(dp[N][0])


if __name__ == "__main__":
    main()
