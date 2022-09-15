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
    N, M = NMI()
    A, B, C, D, E, F = NMI()
    XY = set(tuple(NMI()) for _ in range(M))

    # 移動をそれぞれi, j, k回したときの場合の数
    dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]

    dp[0][0][0] = 1

    for total in range(N):
        for p in range(total+1):
            for q in range(total+1-p):
                r = total - p - q
                X = p * A + q * C + r * E
                Y = p * B + q * D + r * F

                if (X+A, Y+B) not in XY:
                    dp[p+1][q][r] += dp[p][q][r]
                    dp[p+1][q][r] %= MOD99
                if (X+C, Y+D) not in XY:
                    dp[p][q+1][r] += dp[p][q][r]
                    dp[p][q+1][r] %= MOD99
                if (X+E, Y+F) not in XY:
                    dp[p][q][r+1] += dp[p][q][r]
                    dp[p][q][r+1] %= MOD99

    total = N
    ans = 0
    for p in range(total+1):
        for q in range(total+1-p):
            r = total - p - q
            ans += dp[p][q][r]
            ans %= MOD99

    print(ans)


if __name__ == "__main__":
    main()
