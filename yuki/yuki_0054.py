import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    VT = EI(N)
    VT.sort(key=lambda x: x[0]+x[1])
    INF = 10**10
    M = 10000
    dp = [-INF] * (M+1)
    dp2 = [-INF] * (M+1)
    dp[0] = 0
    for i in range(N):
        v, t = VT[i]
        # print(v, t)
        for j in range(M+1):
            if dp[j] < 0:
                continue
            nj = min(M, j+v)
            dp2[j] = max(dp2[j], j, dp[j])
            if j < t:
                dp2[nj] = max(dp2[nj], j+v)
        # print(dp[i+1][:10])
        dp, dp2 = dp2, dp

    print(max(dp))


if __name__ == "__main__":
    main()
