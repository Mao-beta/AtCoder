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
    INF = 10**18
    H = NLI() + [INF] * 5

    dp = [INF] * (N+2)
    dp[0] = 0
    for i in range(N):
        for j in range(1, 3):
            dp[i+j] = min(dp[i+j], dp[i] + abs(H[i] - H[i+j]))
    print(dp[N-1])


if __name__ == "__main__":
    main()
