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
    ABC = EI(3)
    INF = 10**15
    dp = [[-INF] * 4 for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        dp[i + 1][1] = max(dp[i + 1][1], dp[i][0] + ABC[0][i], dp[i][1] + ABC[0][i])
        dp[i + 1][2] = max(dp[i + 1][2], dp[i][1] + ABC[1][i], dp[i][2] + ABC[1][i])
        dp[i + 1][3] = max(dp[i + 1][3], dp[i][2] + ABC[2][i], dp[i][3] + ABC[2][i])
    print(dp[N][3])


if __name__ == "__main__":
    main()
