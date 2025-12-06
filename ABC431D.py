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
    WHB = EI(N)
    INF = 10**15
    M = 0
    for w, h, b in WHB:
        M += w
    M //= 2
    dp = [[-INF]*(M+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i, (w, h, b) in enumerate(WHB):
        for j in range(M+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + b)
            if j+w <= M:
                dp[i+1][j+w] = max(dp[i+1][j+w], dp[i][j] + h)
    print(max(dp[N]))


if __name__ == "__main__":
    main()
