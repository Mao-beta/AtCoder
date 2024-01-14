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
    P = NLI()
    dp = [[0]*(N+2) for _ in range(N+1)]
    dp[0][0] = 1
    for x in range(N, 0, -1):
        i = N-x
        x_idx = P.index(x)
        lim = len(P) - x_idx

        tmp = [0] * (N+2)
        for j in range(i, N+1):
            r = j-i
            # print(i, j, r, lim, x_idx)
            if j-i >= lim:
                tmp[j] += dp[i][j]
                tmp[N+1] -= dp[i][j]
            else:
                tmp[j+1] += dp[i][j]
                tmp[N+1] -= dp[i][j]
        tmp = list(accumulate(tmp))
        # print(tmp)

        tmp = [t % MOD for t in tmp]
        dp[i+1] = tmp

        del P[P.index(x)]
        # print(P)

    print(tmp[-2] % MOD)


if __name__ == "__main__":
    main()
