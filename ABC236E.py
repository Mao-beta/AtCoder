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


def solve_mean(N, A):
    INF = 10**20
    TA = [a*1000 for a in A]
    # 平均値がX以上になるか？
    ok = 0
    ng = 10**15

    # i個選んで、直前のを選んでいない(0)/いる(1)ときの和の最大値

    while abs(ok-ng) > 1:
        X = (ok + ng) // 2
        AA = [a - X for a in TA]

        # AAから2つ以上とばさずに選んで0以上にできるか？
        dp0 = [-INF] * (N+1)
        dp1 = [-INF] * (N+1)
        dp0[0] = 0
        dp1[0] = 0

        for i in range(N):
            a = AA[i]
            # 選ぶ
            dp1[i+1] = max(dp1[i+1], dp0[i] + a, dp1[i] + a)
            # 選ばない
            dp0[i+1] = max(dp0[i+1], dp1[i])

        if max(dp0[-1], dp1[-1]) >= 0:
            ok = X
        else:
            ng = X

    print(ok / 1000)


def solve_median(N, A):
    INF = 10**20
    # 中央値がX以上になるか？
    ok = 0
    ng = 10**10

    # i個選んで、直前のを選んでいない(0)/いる(1)ときの和の最大値

    while abs(ok-ng) > 1:
        X = (ok + ng) // 2
        AA = [1 if a - X >= 0 else -1 for a in A]

        # AAから2つ以上とばさずに選んで0以上にできるか？
        dp0 = [-INF] * (N+1)
        dp1 = [-INF] * (N+1)
        dp0[0] = 0
        dp1[0] = 0

        for i in range(N):
            a = AA[i]
            # 選ぶ
            dp1[i+1] = max(dp1[i+1], dp0[i] + a, dp1[i] + a)
            # 選ばない
            dp0[i+1] = max(dp0[i+1], dp1[i])

        if max(dp0[-1], dp1[-1]) > 0:
            ok = X
        else:
            ng = X

    print(ok)


def main():
    N = NI()
    A = NLI()

    solve_mean(N, A)
    solve_median(N, A)


if __name__ == "__main__":
    main()
