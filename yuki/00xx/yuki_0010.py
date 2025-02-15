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
    T = NI()
    A = NLI()
    # "+"=0, "*"=1として2進数
    INF = 1<<52
    dp = [[INF]*(T+1) for _ in range(N+1)]
    dp[1][A[0]] = 0
    for i in range(1, N):
        a = A[i]
        for j in range(T+1):
            if dp[i][j] >= INF:
                continue
            d = dp[i][j]
            if j+a <= T:
                dp[i+1][j+a] = min(dp[i+1][j+a], d << 1)
            if j*a <= T:
                dp[i+1][j*a] = min(dp[i+1][j*a], (d << 1) | 1)

    print(bin(dp[N][T])[2:].zfill(N-1).replace("0", "+").replace("1", "*"))



if __name__ == "__main__":
    main()
