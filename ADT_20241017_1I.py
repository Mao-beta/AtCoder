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
    S = SI()
    N = len(S)
    dp = [[0]*29 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        s = S[i]
        for j in range(29):
            if dp[i][j] == 0:
                continue
            if j <= 26:
                if s == "?":
                    # 小文字
                    dp[i+1][j] += dp[i][j] * 26
                    # 大文字
                    dp[i+1][j+1] += dp[i][j] * (26-j)
                    dp[i+1][27] += dp[i][j] * j



if __name__ == "__main__":
    main()
