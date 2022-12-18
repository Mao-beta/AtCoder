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
    S = [SI() for _ in range(N)]

    # 最後の単語がiで、使った単語の集合がjのときに勝てるか
    dp = [[-1]*(1<<N) for _ in range(N)]

    def rec(i, j):
        if dp[i][j] != -1:
            return dp[i][j]

        res = 0
        for b in range(N):
            if (j>>b) & 1:
                continue
            if j > 0 and S[i][-1] != S[b][0]:
                continue
            tmp = rec(b, j | (1<<b))
            if tmp == 0:
                res = 1

        dp[i][j] = res
        return res

    if rec(0, 0):
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
