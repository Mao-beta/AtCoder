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
    N = NI()
    P = NLI()[::-1]
    INF = 10**6
    # 最近のほうからi個見ていまj個使っている時の第1項の分子の最大値
    dp = [[-INF]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        p = P[i]
        for j in range(N+1):
            if dp[i][j] <= -INF:
                continue
            c = pow(0.9, j)
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j < N:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + c * p)
    ans = -INF
    b = 1
    for j in range(1, N+1):
        ans = max(ans, dp[N][j] / b - 1200 / math.sqrt(j))
        b += pow(0.9, j)

    print(ans)


if __name__ == "__main__":
    main()
