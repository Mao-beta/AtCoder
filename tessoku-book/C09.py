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
    dp = [[0]*2 for _ in range(N+1)]
    for i in range(N):
        a = A[i]
        for j in range(2):
            dp[i+1][0] = max(dp[i])
            dp[i+1][1] = dp[i][0] + a
    print(max(dp[-1]))


if __name__ == "__main__":
    main()