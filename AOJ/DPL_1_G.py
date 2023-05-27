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
    VW = []
    for _ in range(N):
        v, w, m = NMI()
        x = 1
        while x <= m:
            VW.append([v*x, w*x])
            m -= x
            x *= 2
        if m > 0:
            VW.append([v*m, w*m])

    N = len(VW)
    INF = 10**15
    dp = [[-INF]*(W+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i, (v, w) in enumerate(VW):
        for j in range(W+1):
            d = dp[i][j]
            if d < 0:
                continue

            dp[i+1][j] = max(dp[i+1][j], d)
            if j+w <= W:
                dp[i+1][j+w] = max(dp[i+1][j+w], d+v)

    print(max(dp[-1]))


if __name__ == "__main__":
    main()
