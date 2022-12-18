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
    A = NLI()
    dp = [[0, 0] for _ in range(N+1)]
    dp[0][0] = 0
    dp[0][1] = 1
    for i in range(N):
        dp[i+1][1] = dp[i][0] + dp[i][1]
        dp[i+1][0] = dp[i][1]
        dp[i+1][0] %= MOD
        dp[i+1][1] %= MOD

    rdp = dp[::-1]

    ans = 0
    for i in range(N):
        ans += (sum(rdp[i+1]) * dp[i][1] - rdp[i+1][1] * dp[i][0]) * A[i]
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
