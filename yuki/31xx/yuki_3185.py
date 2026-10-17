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
    T = NI()
    INF = 10**18
    for _ in range(T):
        N = NI()
        A = NLI()
        # i個見て直前がj組目で反転があるか(k)
        dp = [[[-INF]*2 for _ in range(3)] for _ in range(N+1)]
        dp[0][0][0] = 0
        for i in range(N):
            a = A[i]
            for j in range(3):
                for k in range(2):
                    d = dp[i][j][k]
                    if d <= -INF:
                        continue
                    if i == 0:
                        dp[i+1][0][0] = d + a
                        dp[i+1][0][1] = d - a
                        continue
                    for nj in range(j, j+2):
                        if nj >= 3:
                            continue
                        for nk in range(2):
                            if j == nj and k != nk:
                                continue
                            dp[i+1][nj][nk] = max(dp[i+1][nj][nk], d + a * (1-2*nk))
        print(max(dp[N][2]))


if __name__ == "__main__":
    main()
