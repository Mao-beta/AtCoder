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
    XYZ = EI(N)
    # dp[i][j]: i個の選挙区を見て、j議席取っているときの最小値
    INF = 10**20
    dp = [[INF]*200005 for _ in range(N+1)]
    dp[0][0] = 0
    Z = 0
    for i in range(N):
        x, y, z = XYZ[i]
        Z += z
        for j in range(100001):
            k = max((y-x+1) // 2, 0)
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            dp[i+1][j+z] = min(dp[i+1][j+z], dp[i][j] + k)

    ans = INF
    for j in range((Z+1)//2, Z+1):
        ans = min(ans, dp[-1][j])
    print(ans)


if __name__ == "__main__":
    main()
