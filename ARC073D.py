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
    N, W = NMI()
    WV = [NLI() for _ in range(N)]

    dp = [defaultdict(int) for _ in range(N+1)]
    for i in range(N):
        w, v = WV[i]
        dp[i][0] = 0

        for j in list(dp[i].keys()):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j+w <= W:
                dp[i+1][j+w] = max(dp[i+1][j+w], dp[i][j] + v)

    print(max(dp[-1].values()))


if __name__ == "__main__":
    main()
