import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    # 両方ある/上がない/下がない
    dp = [[0]*3 for _ in range(N+2)]
    dp[0][0] = 1
    for i in range(N):
        d0, d1, d2 = dp[i]
        dp[i+1][0] += d0
        dp[i+2][0] += d0
        dp[i+2][1] += d0
        dp[i+2][2] += d0

        dp[i+1][2] += d1
        dp[i+1][0] += d1

        dp[i+1][1] += d2
        dp[i+1][0] += d2

    print(dp[N][0])


if __name__ == "__main__":
    main()
