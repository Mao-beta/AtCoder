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

    A = [[j, i] for i, j in enumerate(A)]
    A.sort(reverse=True)
    # print(A)

    # i人まで決めてj人が左よせ
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        a, idx = A[i]
        for j in range(i+1):
            # print(i, j, i-j, N - (i-j))
            # 左に寄せる
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + a * abs(idx - j))
            # 右に寄せる
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + a * abs(idx - (N-1 - (i-j))))

    # print(*dp, sep="\n")
    print(max(dp[-1]))


if __name__ == "__main__":
    main()
