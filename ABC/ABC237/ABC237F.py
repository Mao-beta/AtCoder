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
    dp = [[[[0]*(N+1) for _ in range(M+1)] for _ in range(M+1)] for _ in range(M+1)]
    dp[M][M][M][0] = 1

    for i in range(N):
        for a in range(M+1):
            for b in range(M+1):
                for c in range(M+1):
                    for x in range(M):
                        if x <= a:
                            dp[x][b][c][i+1] += dp[a][b][c][i]
                            dp[x][b][c][i+1] %= MOD99
                        elif x <= b:
                            dp[a][x][c][i+1] += dp[a][b][c][i]
                            dp[a][x][c][i+1] %= MOD99
                        elif x <= c:
                            dp[a][b][x][i+1] += dp[a][b][c][i]
                            dp[a][b][x][i+1] %= MOD99

    ans = 0
    for a in range(M):
        for b in range(M):
            for c in range(M):
                ans += dp[a][b][c][-1]
                ans %= MOD99
    print(ans)


if __name__ == "__main__":
    main()
