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
    N, K = NMI()
    A = NLI()

    INF = 10**10
    dp = [[0, INF] for _ in range(N+1)]
    dp[0][1] = 0
    for i in range(N+1):
        for j in range(2):
            for a in A:
                if i < a:
                    break

                if j == 0:
                    dp[i][j] = max(dp[i][j], dp[i-a][1-j] + a)
                else:
                    dp[i][j] = min(dp[i][j], dp[i-a][1-j])

    print(dp[N][0])


if __name__ == "__main__":
    main()
