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
    X, Y = NMI()
    N = NI()
    TH = EI(N)
    # dp[i][j][k]: i個みてj個買ってk枚残っている
    dp = [[-1]*(X+Y+1) for _ in range(X+1)]
    dp[0][X+Y] = 0
    for i in range(N):
        t, h = TH[i]
        dp2 = [[-1] * (X + Y + 1) for _ in range(X + 1)]
        for j in range(X+1):
            for k in range(X+Y+1):
                d = dp[j][k]
                if d < 0:
                    continue
                dp2[j][k] = max(dp2[j][k], d)
                if k >= t and j < X:
                    # print(i, j, k)
                    dp2[j+1][k-t] = max(dp2[j+1][k-t], d + h)
        dp, dp2 = dp2, dp

    ans = 0
    for j in range(X+1):
        for k in range(X+Y+1):
            ans = max(ans, dp[j][k])

    # print(*dp, sep="\n")
    print(ans)


if __name__ == "__main__":
    main()
