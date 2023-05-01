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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N, K = NMI()
    A = sorted(NLI(), reverse=True)
    # dp[i][t]: i個みて、高橋君の操作回数がt回のときの最小本数
    INF = 10**10
    dp = [[INF]*32 for _ in range(N+1)]
    dp[0][0] = 0
    
    R = A[::-1]
    
    for i in range(N):
        a = A[i]
        idx = N - bisect.bisect_right(R, a//2)

        for t in range(31):
            d = dp[i][t]
            if d > K:
                continue
            # 抜く
            if d < K:
                dp[i+1][t] = min(dp[i+1][t], d + 1)
            # 抜かない
            dp[idx][t+1] = min(dp[idx][t+1], d)

    for t in range(32):
        a = dp[-1][t]
        if a < INF:
            print(t, a)
            exit()


if __name__ == "__main__":
    main()
