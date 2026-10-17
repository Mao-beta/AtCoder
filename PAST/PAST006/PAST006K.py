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
    PU = EI(N)
    INF = 10**20
    dp = [[-INF]*100 for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        p, u = PU[i]
        for j in range(100):
            if dp[i][j] <= -INF:
                continue
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            nj = (j+p) % 100
            dp[i+1][nj] = max(dp[i+1][nj], dp[i][j] + u - p + (j+p)//100 * 20)

    print(max(dp[N]))


if __name__ == "__main__":
    main()
