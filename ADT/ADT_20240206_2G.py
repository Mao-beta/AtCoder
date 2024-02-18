import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    N, L, R = NMI()
    A = NLI()
    INF = 10**18

    # 左からi個決めて、まだLに変えても良いか(j)
    dp = [[INF]*2 for _ in range(N+1)]
    dp[0][1] = 0
    for i in range(N):
        for j in range(2):
            dp[i+1][0] = min(dp[i+1][0], dp[i][j] + A[i])
            if j == 1:
                dp[i+1][1] = min(dp[i+1][1], dp[i][j] + L)

    B = A[::-1]
    # 左からi個決めて、まだRに変えても良いか(j)
    dp2 = [[INF] * 2 for _ in range(N + 1)]
    dp2[0][1] = 0
    for i in range(N):
        for j in range(2):
            dp2[i + 1][0] = min(dp2[i + 1][0], dp2[i][j] + B[i])
            if j == 1:
                dp2[i + 1][1] = min(dp2[i + 1][1], dp2[i][j] + R)
    dp2 = dp2[::-1]

    ans = INF
    for i in range(N+1):
        ans = min(ans, min(dp[i]) + min(dp2[i]))
    print(ans)


if __name__ == "__main__":
    main()
