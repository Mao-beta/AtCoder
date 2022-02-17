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
    N, A = NMI()
    X = NLI()
    X = [x-A for x in X] # -49 ... 49

    dp = [[0]*5001 for _ in range(N+1)] # -2500...2500 -> 0...5000
    dp[0][2500] = 1

    for i in range(N):
        x = X[i]
        for j in range(-2500, 2501):
            dp[i+1][j+2500] += dp[i][j+2500]
            if 0 <= j+2500+x <= 5000:
                dp[i+1][j+2500+x] += dp[i][j+2500]

    print(dp[-1][2500]-1)


if __name__ == "__main__":
    main()
