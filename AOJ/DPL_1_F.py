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
    N, W = NMI()
    VW = EI(N)
    INF = 10**15
    # dp[i][j]: i個決めて価値の合計がjのときの重さの最小値
    dp = [[INF]*10001 for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        v, w = VW[i]
        for j in range(10001):
            now = dp[i][j]
            if now == INF:
                continue
            dp[i+1][j] = min(dp[i+1][j], now)
            if now + w <= W:
                dp[i+1][j+v] = min(dp[i+1][j+v], now+w)

    ans = 0
    for v in range(10001):
        if dp[-1][v] <= W:
            ans = v
    print(ans)


if __name__ == "__main__":
    main()
