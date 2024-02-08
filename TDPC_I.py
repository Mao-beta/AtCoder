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
    S = SI()
    N = len(S)

    dp = [[0] * (N+1) for _ in range(N+1)]
    oks = [[0] * (N+1) for _ in range(N+1)]

    for l in range(N, -1, -1):
        for r in range(l, N + 1):
            if r-l == 0:
                oks[l][r] = 1
                continue
            if r-l <= 2:
                continue

            for m in range(l + 1, r):
                dp[l][r] = max(dp[l][r], dp[l][m] + dp[m][r])
                if oks[l][m] and oks[m][r]:
                    oks[l][r] = 1

            if r-l >= 3:
                if S[l] != "i" or S[r-1] != "i":
                    continue
                for w in range(l+1, r-1):
                    if S[w] != "w":
                        continue
                    if oks[l+1][w] and oks[w+1][r-1]:
                        dp[l][r] = max(dp[l][r], dp[l+1][w] + dp[w+1][r-1] + 1)
                        oks[l][r] = 1

    print(dp[0][N])


if __name__ == "__main__":
    main()
