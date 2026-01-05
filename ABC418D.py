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
    T = SI()
    # i個見て、そこまでで0/1(=j)となるそれより左の連続部分列の個数
    dp = [[0]*2 for _ in range(N+1)]
    if T[0] == "0":
        dp[1][0] = 1
    else:
        dp[1][1] = 1
    for i in range(1, N):
        if T[i] == "0":
            dp[i+1][0] = dp[i][1] + 1
            dp[i+1][1] = dp[i][0]
        else:
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][1] + 1
    ans = 0
    for i in range(N+1):
        ans += dp[i][1]
    print(ans)


if __name__ == "__main__":
    main()
