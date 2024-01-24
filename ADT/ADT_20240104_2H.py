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
    H, W, K = NMI()
    x1, y1, x2, y2 = NMI()
    dp = [[0]*4 for _ in range(K+1)]
    if x1 != x2 and y1 != y2:
        dp[0][0] = 1
    elif x1 != x2 and y1 == y2:
        dp[0][1] = 1
    elif x1 == x2 and y1 != y2:
        dp[0][2] = 1
    else:
        dp[0][3] = 1

    A = [[H+W-4, 1, 1, 0],
         [W-1, H-2, 0, 1],
         [H-1, 0, W-2, 1],
         [0, H-1, W-1, 0]]

    for i in range(K):
        for p in range(4):
            for q in range(4):
                dp[i+1][q] += dp[i][p] * A[p][q] % MOD99
        for j in range(4):
            dp[i+1][j] %= MOD99

    print(dp[-1][-1])


if __name__ == "__main__":
    main()
