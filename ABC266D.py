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
    TXA = [NLI() for _ in range(N)]

    C = [[0]*5 for _ in range(10**5+5)]

    for t, x, a in TXA:
        C[t][x] = a

    INF = 10**20
    # dp[i][j] i秒後にjにいるときのmax
    dp = [-INF] * 5
    dp[0] = 0

    for i in range(10**5+1):
        dp2 = [-INF] * 5
        for j in range(5):
            if dp[j] < 0: continue
            for k in range(-1, 2):
                nj = j + k
                if nj < 0 or nj >= 5: continue

                dp2[nj] = max(dp2[nj], dp[j] + C[i+1][nj])

        dp, dp2 = dp2, dp

    print(max(dp))


if __name__ == "__main__":
    main()
