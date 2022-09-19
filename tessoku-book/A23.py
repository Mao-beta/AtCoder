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
    N, M = NMI()
    A = [int(SI().replace(" ", ""), base=2) for _ in range(M)]
    dp = [[1000]*(1<<N) for _ in range(M+1)]
    dp[0][0] = 0
    for i in range(M):
        a = A[i]
        for j in range(1<<N):
            x = dp[i][j]
            dp[i+1][j] = min(dp[i+1][j], x)
            dp[i+1][j|a] = min(dp[i+1][j|a], x+1)
    ans = dp[-1][-1]
    print(ans if ans < 1000 else -1)


if __name__ == "__main__":
    main()
