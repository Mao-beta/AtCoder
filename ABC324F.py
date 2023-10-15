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
    N, M = NMI()
    UVBC = EI(M)
    UVBC = [[x-1, y-1, b, c] for x, y, b, c in UVBC]
    UVBC.sort()
    INF = 10**10

    def judge(X):
        # sumB/sumCがX以上で通れるか？
        # sum(b - cX) >= 0
        # dp[v]: vに到達したときのsum(b - cX)の最大値
        dp = [-INF] * N
        dp[0] = 0
        for u, v, b, c in UVBC:
            t = b - c * X
            dp[v] = max(dp[v], dp[u] + t)

        return dp[N-1] >= 0

    ok = 0
    ng = 10**10
    for _ in range(80):
        X = (ok + ng) / 2
        if judge(X):
            ok = X
        else:
            ng = X

    print(ok)


if __name__ == "__main__":
    main()
