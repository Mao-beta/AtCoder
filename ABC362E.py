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
    N = NI()
    A = NLI()
    if N == 1:
        print(N)
        return
    if N == 2:
        print(N, N * (N-1) // 2)
        return
    ans = [0] * (N+1)
    ans[1] = N
    ans[2] = N * (N-1) // 2
    for x in range(N):
        for y in range(x+1, N):
            # 初項がAxとAy
            # i個見て、k個採用している
            dp = [[0]*(N+1) for _ in range(N+1)]
            dp[y+1][2] = 1
            for i in range(y+1, N):
                a = A[i]
                for k in range(2, N+1):
                    dp[i+1][k] += dp[i][k]
                    dp[i+1][k] %= MOD99
                    # 次はAx+(Ay-Ax)*k
                    if k < N and a == A[x] + (A[y]-A[x])*k:
                        # print(x, y, i, k)
                        dp[i+1][k+1] += dp[i][k]
                        dp[i+1][k+1] %= MOD99
            # print(x, y)
            # print(*dp, sep="\n")
            for k in range(3, N+1):
                ans[k] += dp[N][k]
                ans[k] %= MOD99
    print(*ans[1:])



if __name__ == "__main__":
    main()
