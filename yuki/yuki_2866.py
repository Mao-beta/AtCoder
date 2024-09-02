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
    N, W = NMI()
    VW = EI(N)
    VW.sort(key=lambda x: x[1])
    INF = 10**18
    M = 30000
    # dp[i][j]: i個みて、重さjのときのMax評価値と個数
    dp = [[[-INF, 0] for _ in range(M)] for _ in range(N+1)]
    dp[0][0][0] = 0
    dp[0][0][1] = 1
    for i, (v, w) in enumerate(VW):
        # print(f"{i=} {v=} {w=}")
        for j in range(-10000, 10001):
            dv, dk = dp[i][j]
            # if dk > 0:
            #     print(i, j, v, w, dv, dk)
            nv, nk = dp[i+1][j]
            if dv > nv:
                dp[i+1][j] = [dv, dk]
            elif dv == nv:
                dp[i+1][j][1] += dk
                dp[i+1][j][1] %= MOD99

            if j + w > W:
                continue

            # if dk > 0:
            #     print(f"# {i=} {j=} {v=} {w=} {j+w=} {dv=} {dv+v=} {dk=}")

            nv, nk = dp[i+1][j+w]
            if dv+v > nv:
                dp[i+1][j+w] = [dv+v, dk]
            elif dv+v == nv:
                dp[i+1][j+w][1] += dk
                dp[i+1][j+w][1] %= MOD99

    # for i in range(N+1):
    #     print(dp[i][0])

    tv = -INF
    for j in range(M):
        tv = max(tv, dp[-1][j][0])
    ans = 0
    for j in range(M):
        v, k = dp[-1][j]
        if v == tv:
            # print(j, v, k)
            ans += k
    print(tv, ans % MOD99)


if __name__ == "__main__":
    main()
