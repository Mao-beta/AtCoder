import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    N = NI()
    A = NLI()
    INF = 10**18

    if N == 2:
        print(min(A))
        return
    if N == 3:
        print(sum(A) - max(A))
        return

    # A0 ~ A_N-2までで何とかする
    # dp[i][j]: i個見て、直前にあげているか(j)
    dp = [INF] * (N+2)
    dp[0] = 0
    for i in range(N):
        dp[i+1] = min(dp[i+1], dp[i] + A[i])

    ans = dp[N]

    # ずらす
    dp = [INF] * (N + 2)
    A = A[1:] + [A[0]]
    dp[0] = 0
    for i in range(N):
        dp[i + 2] = min(dp[i + 2], dp[i] + A[i])
        if i > 0:
            dp[i + 1] = min(dp[i + 1], dp[i] + A[i - 1])

    ans = min(ans, dp[N])
    print(ans)


if __name__ == "__main__":
    main()
