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

    INF = 10**15
    dp = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][i] = 0

    def rec(l, r):
        if dp[l+1][r] == INF:
            lp = rec(l + 1, r)
        else:
            lp = dp[l+1][r]

        if dp[l][r-1] == INF:
            rp = rec(l, r - 1)
        else:
            rp = dp[l][r-1]

        # 太郎
        if (N - (r - l)) % 2 == 0:
            res = max(lp + A[l], rp + A[r - 1])
        # 次郎
        else:
            res = min(lp - A[l], rp - A[r - 1])

        dp[l][r] = res
        return res

    ans = rec(0, N)
    print(ans)


if __name__ == "__main__":
    main()
