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
    N, M = NMI()
    ABC = EI(N)
    B2AC = [[] for _ in range(5001)]
    for a, b, c in ABC:
        B2AC[b].append([a, c])
    INF = 10**20
    dp = [INF] * 5001
    dp[0] = 0
    for b in range(5001):
        dp2 = dp[:]
        for i in range(5001):
            for a, c in B2AC[b]:
                dp2[min(i+c, 5000)] = min(dp2[min(i+c, 5000)], dp[i] + a)
        dp, dp2 = dp2, dp
    ans = min(dp[M:])
    print(ans if ans < INF else -1)


if __name__ == "__main__":
    main()
