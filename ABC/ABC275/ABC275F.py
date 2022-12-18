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

    INF = 5000
    # dp[r][i][x] i個まで見て（r: 最後の項を採用しているか）和がxのときの最小回数
    dp = [[[INF]*(M+1) for i in range(N+1)] for r in range(2)]
    dp[1][0][0] = 0

    for i in range(N):
        a = A[i]
        for x in range(M+1):
            for r in range(2):
                k = dp[r][i][x]
                for nr in range(2):
                    if nr == 1:
                        nx = x + a
                    else:
                        nx = x
                    if nx > M:
                        continue

                    dp[nr][i+1][nx] = min(dp[nr][i+1][nx], k + int(r and not nr))

    for x in range(1, M+1):
        ans = min(dp[0][-1][x], dp[1][-1][x])
        print(ans if ans < INF else -1)


if __name__ == "__main__":
    main()
