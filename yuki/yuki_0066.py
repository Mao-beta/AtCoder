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
    M = NI()
    N = 1<<M
    S = [NI() for _ in range(N)]
    dp = [[0]*N for _ in range(M+1)]
    dp[0] = [1] * N
    for m in range(M):
        B = 1<<(m+1)
        for l in range(0, N, B):
            mid = l + B//2
            r = l + B
            for i in range(l, mid):
                for j in range(mid, r):
                    si, sj = S[i], S[j]
                    pi = si**2 / (si**2 + sj**2)
                    pj = sj**2 / (si**2 + sj**2)
                    dp[m+1][i] += dp[m][j] * pi * dp[m][i]
                    dp[m+1][j] += dp[m][i] * pj * dp[m][j]
    print(dp[M][0])


if __name__ == "__main__":
    main()
