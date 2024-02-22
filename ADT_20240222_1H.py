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
    S = SI()
    dp = [[0, 0] for _ in range(N)]
    dp[0][int(S[0])] = 1
    for i in range(1, N):
        s = int(S[i])
        for j in range(2):
            nj = 1
            if j == s == 1:
                nj = 0
            dp[i][nj] += dp[i-1][j]
        dp[i][s] += 1

    ans = 0
    for i in range(N):
        ans += dp[i][1]
    print(ans)


if __name__ == "__main__":
    main()
