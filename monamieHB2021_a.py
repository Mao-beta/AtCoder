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
    ans = 0
    M = 520
    N %= 520
    INF = 10**10
    dp = [INF] * M
    dp[0] = 0
    for i in range(M):
        for l in [8, 10, 26]:
            if i+l < M:
                dp[i+l] = min(dp[i+l], dp[i] + int(l != 26))
    print(dp[N])


if __name__ == "__main__":
    main()
