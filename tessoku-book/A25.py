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
    H, W = NMI()
    G = [SI() for _ in range(H)]

    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for h in range(H):
        for w in range(W):
            if G[h][w] == "#":
                continue
            if h > 0:
                dp[h][w] += dp[h-1][w]
            if w > 0:
                dp[h][w] += dp[h][w-1]
    print(dp[-1][-1])


if __name__ == "__main__":
    main()
