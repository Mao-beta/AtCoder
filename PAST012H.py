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
    N, X = NMI()
    ABC = EI(N)
    INF = 10**9
    dp = [[(-INF, -INF) for _ in range(X+1)] for _ in range(N+1)]
    dp[0][X] = (0, INF)
    for i in range(N):
        a, b, c = ABC[i]
        for j in range(X+1):
            g, s = dp[i][j]
            if g < -1:
                continue

            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j >= b:
                g += c
                s -= a
                dp[i+1][j-b] = max(dp[i+1][j-b], (g, s))

    ans = (-INF, -INF)
    ans_x = -1
    for x in range(X+1):
        g, s = dp[-1][x]
        if (g, s) >= ans:
            ans = (g, s)
            ans_x = x

    print(*ans, ans_x)


if __name__ == "__main__":
    main()
