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
    N, M = NMI()
    A = NLI()
    INF = 10**15
    # dp[i][j] i個まで見てj個選んでいるときの最大
    dp = [[-INF]*(M+1) for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        a = A[i]
        for j in range(M+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j < M:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + a * (j+1))

    print(dp[-1][-1])


if __name__ == "__main__":
    main()
