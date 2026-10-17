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
    N, M = NMI()
    A = NLI()
    INF = 10**18
    # i日みてj日宿題して昨日宿題したか(k)
    dp = [[[-INF]*2 for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(i+1):
            for k in range(2):
                if dp[i][j][k] < 0:
                    continue
                dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j][k] + A[i])
                if k == 0:
                    dp[i+1][j+1][1] = max(dp[i+1][j+1][1], dp[i][j][k])
    ans = 0
    for j in range(M, N+1):
        for k in range(2):
            ans = max(ans, dp[N][j][k])
    print(ans)


if __name__ == "__main__":
    main()
