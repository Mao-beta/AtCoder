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
    N, P = NMI()
    dp = [[0]*N for _ in range(N+1)]
    dp[0][0] = 1

    D = [0] * 6
    W = [10**i for i in range(6)]

    for j in range(2, N):
        for i in range(6):
            D[i] = 0

        for i in range(1, N+1):
            for k in range(2, 6):
                if j < k: continue
                if i >= W[k-1]:
                    D[k] += dp[i-W[k-2]][j-k] - dp[i-W[k-1]][j-k]
                elif i >= W[k-2]:
                    # print(k, i, i-10**(k-2), j-k)
                    D[k] += dp[i-W[k-2]][j-k]
                D[k] %= P

            dp[i][j] += sum(D) % P * 25 % P

            if i <= 9 and j == 2:
                dp[i][j] += 1
            elif 10 <= i <= 99 and j == 3:
                dp[i][j] += 1
            elif 100 <= i <= 999 and j == 4:
                dp[i][j] += 1
            elif 1000 <= i and j == 5:
                dp[i][j] += 1

            dp[i][j] %= P

    print(sum(dp[-1]) % P)


if __name__ == "__main__":
    main()
