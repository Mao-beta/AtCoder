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
    N, K, D = NMI()
    A = NLI()
    INF = 10**15

    # i個見てj個使ってて余りがkのときの総和
    dp = [[[-INF]*D for _ in range(K+1)] for _ in range(N+1)]
    dp[0][0][0] = 0

    for i in range(N):
        a = A[i]
        for j in range(K+1):
            for k in range(D):
                # 使わない
                dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])
                # 使う
                if j < K:
                    dp[i+1][j+1][(k+a)%D] = max(dp[i+1][j+1][(k+a)%D], dp[i][j][k] + a)

    ans = dp[-1][K][0]
    # print(*dp, sep="\n")
    print(ans if ans >= 0 else -1)


if __name__ == "__main__":
    main()
