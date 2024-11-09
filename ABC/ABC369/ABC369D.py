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
    INF = 10**10
    dp = [[-INF]*2 for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        a = A[i]
        for j in range(2):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            dp[i+1][j^1] = max(dp[i+1][j^1], dp[i][j] + a * (1 + j))
    print(max(dp[-1]))


if __name__ == "__main__":
    main()
