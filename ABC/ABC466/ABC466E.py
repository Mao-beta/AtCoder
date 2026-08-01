import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N, K = NMI()
    AB = EI(N)
    INF = 10**18
    dp = [[[-INF]*2 for _ in range(K+1)] for _ in range(N+1)]
    dp[0][0][0] = 0
    for i in range(N):
        a, b = AB[i]
        for j in range(K+1):
            for k in range(2):
                if j == K and k == 1:
                    continue
                d = dp[i][j][k]
                if d < 0:
                    continue
                if k == 0:
                    dp[i+1][j][0] = max(dp[i+1][j][0], d+a)
                    if j < K:
                        dp[i+1][j][1] = max(dp[i+1][j][1], d+b)
                else:
                    if j < K:
                        dp[i+1][j+1][0] = max(dp[i+1][j+1][0], d+a)
                    dp[i+1][j][1] = max(dp[i+1][j][1], d+b)
    ans = 0
    for j in range(K+1):
        for k in range(2):
            ans = max(ans, dp[N][j][k])
    print(ans)


if __name__ == "__main__":
    main()
