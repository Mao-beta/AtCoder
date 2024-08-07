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
    N, K = NMI()
    H = NLI()
    INF = 10**10

    if K == N:
        print(0)
        return

    # 左からi個見て直前の高さがHjで操作回数がk
    dp = [[[INF]*(K+1) for _ in range(N)] for _ in range(N+1)]
    for j in range(N):
        if j == 0:
            k = 0
        else:
            k = 1
            if K == 0:
                continue
        dp[1][j][k] = H[j]

    for i in range(1, N):
        hi = H[i]
        for j in range(N):
            hj = H[j]
            for k in range(K+1):
                # 変えない
                plus = max(0, hi-hj)
                dp[i+1][i][k] = min(dp[i+1][i][k],
                                    dp[i][j][k] + plus)
                if k == K:
                    continue
                # 引き継ぐ
                dp[i+1][j][k+1] = min(dp[i+1][j][k+1],
                                      dp[i][j][k])
                # if i == N-1:
                #     continue
                # # 次のにする
                # plus = max(0, H[i+1]-hj)
                # dp[i+1][i+1][k+1] = min(dp[i+1][i+1][k+1],
                #                         dp[i][j][k] + plus)

    ans = INF
    for j in range(N):
        ans = min(ans, min(dp[N][j]))

    print(ans)


if __name__ == "__main__":
    main()
