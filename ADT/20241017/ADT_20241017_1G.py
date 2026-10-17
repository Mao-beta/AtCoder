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
    XYZ = EI(N)
    INF = 10**15
    M = 10**5
    dp = [[INF]*(M+1) for _ in range(N+1)]
    dp[0][0] = 0
    Zsum = 0
    for i in range(N):
        x, y, z = XYZ[i]
        Zsum += z
        for j in range(M+1):
            d = dp[i][j]
            if d >= INF:
                continue
            if x > y:
                dp[i+1][j+z] = min(dp[i+1][j+z], d)
            else:
                t = (x+y+1) // 2
                dp[i+1][j+z] = min(dp[i+1][j+z], d + t-x)
                dp[i+1][j] = min(dp[i+1][j], d)
    print(min(dp[N][(Zsum+1)//2:]))


if __name__ == "__main__":
    main()
