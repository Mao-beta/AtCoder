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
    V = NLI()
    INF = 10**10
    dp = [[-INF]*2 for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(1, N+1):
        v = V[i-1]
        dp[i][0] = max(dp[i][0], dp[i-1][0], dp[i-1][1])
        dp[i][1] = max(dp[i][1], dp[i-1][0] + v)
    print(max(dp[N]))


if __name__ == "__main__":
    main()
