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
    N, H = NMI()
    X = [0] + NLI()
    PF = EI(N-1) + [[0, 0]]
    INF = 10**18
    dp = [[[INF]*(H+1) for _ in range(H+1)] for _ in range(N+1)]

    for k in range(H+1):
        dp[0][H][k] = 0

    for i in range(N):
        p, f = PF[i]
        d = X[i+1] - X[i]
        for j in range(d, H+1):
            for k in range(H+1-d):
                if dp[i][j][k] >= INF:
                    continue
                # print(i, j, k, dp[i][j][k])
                # 使わない
                dp[i+1][j-d][k+d] = min(dp[i+1][j-d][k+d], dp[i][j][k])
                # 行きに使う
                nj = min(j-d+f, H)
                if nj >= 0:
                    dp[i+1][nj][k+d] = min(dp[i+1][nj][k+d], dp[i][j][k] + p)
                # 帰りに使う
                nk = k+d-f
                if nk >= 0:
                    dp[i+1][j-d][nk] = min(dp[i+1][j-d][nk], dp[i][j][k] + p)

    # print(*dp[-1], sep="\n")
    ans = INF
    d = X[-1] - X[-2]
    for j in range(d, H+1):
        ans = min(ans, dp[-1][j][j])

    if ans >= INF:
        ans = -1
    print(ans)


if __name__ == "__main__":
    main()
