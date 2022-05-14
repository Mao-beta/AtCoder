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
    A = NLI()
    INF = 10**20
    ans = INF

    # i個目の餌やリまで決めたときのコスト最小値
    # jは直前に餌をやったかどうか
    # kは最初に餌をやったかどうか
    dp = [[[INF]*2 for _ in range(2)] for _ in range(N+1)]
    dp[1][0][0] = 0
    dp[1][1][1] = A[0]

    for i in range(1, N):
        a = A[i]

        for k in range(2):
            # 今回やらないときは前回やったときのみ
            dp[i+1][0][k] = min(dp[i+1][0][k], dp[i][1][k])
            # 今回やる
            dp[i+1][1][k] = min(dp[i+1][1][k], dp[i][0][k] + a, dp[i][1][k] + a)

    for j in range(2):
        for k in range(2):
            if k == 0 and j == 0:
                continue
            ans = min(ans, dp[-1][j][k])

    print(ans)


if __name__ == "__main__":
    main()
