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


def main(N, P):
    # M[l][r]: [l, r)の最大値のindex
    M = [[-1]*(N+1) for _ in range(N+1)]

    for g in range(1, N+1):
        for l in range(N-g+1):
            r = l + g
            if g == 1:
                M[l][r] = l
            else:
                x, y = M[l][r-1], M[l+1][r]
                if P[x] > P[y]:
                    M[l][r] = x
                else:
                    M[l][r] = y

    print(*M, sep="\n")

    memo = [[-1] * (N + 1) for _ in range(N + 1)]
    for i in range(N+1):
        memo[i][i] = 1
    for i in range(N):
        memo[i][i+1] = 1

    def rec(l, r):

        if r - l <= 1:
            memo[l][r] = 1
            return 1
        m = M[l][r]
        print(l, r, m)
        sl = 0
        sr = 0
        for nl in range(l, m):
            if memo[l][nl] == -1:
                sl += rec(l, nl)
            else:
                sl += memo[l][nl]

        for nr in range(m+1, r):
            if memo[nr][r] == -1:
                sr += rec(nr, r)
            else:
                sr += memo[nr][r]

        if sl == 0:
            sl = 1
        if sr == 0:
            sr = 1

        res = sl * sr % MOD99
        print(l, r, sl, sr, res)
        memo[l][r] = res
        return res

    rec(0, N)
    print(*memo, sep="\n")


if __name__ == "__main__":
    N = NI()
    P = NLI()
    main(N, P)
