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
    X, Y, Z = NMI()
    S = SI()
    N = len(S)
    S = [int(s == "A") for s in S]
    INF = 10**18
    dp = [[INF]*2 for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        s = S[i]
        for j in range(2):
            d = dp[i][j]
            if s == j:
                dp[i+1][j] = min(dp[i+1][j], d+X)
                dp[i+1][j^1] = min(dp[i+1][j^1], d+Z+Y)
            else:
                dp[i+1][j] = min(dp[i+1][j], d+Y)
                dp[i+1][j^1] = min(dp[i+1][j^1], d+Z+X)

    print(min(dp[-1]))


if __name__ == "__main__":
    main()
