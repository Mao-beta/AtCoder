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
    N = NI()
    A = NLI()

    ans = 0
    # k個選ぶ
    for k in range(1, N+1):
        if k == 1:
            ans += N
            continue

        # dp[i][j][m] i個まで見てj個使って余りがm
        dp = [[[0]*k for _ in range(N+1)] for _ in range(N+1)]
        dp[0][0][0] = 1
        for i, a in enumerate(A):
            a %= k
            for j in range(k+1):
                for m in range(k):
                    if dp[i][j][m] == 0: continue
                    dp[i+1][j][m] += dp[i][j][m]
                    dp[i+1][j][m] %= MOD99
                    dp[i+1][j+1][(m+a)%k] += dp[i][j][m]
                    dp[i+1][j+1][(m+a)%k] %= MOD99

        ans += dp[-1][k][0]
        ans %= MOD99
        # print(*dp, sep="\n")
        # print(dp[-1])
    print(ans)


if __name__ == "__main__":
    main()
