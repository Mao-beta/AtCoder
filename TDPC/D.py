import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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
    N, D = NMI()

    d = D
    c2 = 0
    c3 = 0
    c5 = 0
    while d % 2 == 0:
        d //= 2
        c2 += 1

    while d % 3 == 0:
        d //= 3
        c3 += 1

    while d % 5 == 0:
        d //= 5
        c5 += 1

    if d != 1:
        print(0)
        exit()

    dp = [[[[0]*(c5+1) for _ in range(c3+1)] for _ in range(c2+1)] for _ in range(N+1)]
    dp[0][0][0][0] = 1

    dice2 = [0, 1, 0, 2, 0, 1]
    dice3 = [0, 0, 1, 0, 0, 1]
    dice5 = [0, 0, 0, 0, 1, 0]

    for i in range(N):
        for a in range(c2+1):
            for b in range(c3+1):
                for c in range(c5+1):
                    if dp[i][a][b][c] == 0:
                        continue
                    for da, db, dc in zip(dice2, dice3, dice5):
                        na = min(c2, a+da)
                        nb = min(c3, b+db)
                        nc = min(c5, c+dc)
                        dp[i+1][na][nb][nc] += dp[i][a][b][c] / 6

    print(dp[-1][-1][-1][-1])


if __name__ == "__main__":
    main()
