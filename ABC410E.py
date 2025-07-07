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
    N, H, M = NMI()
    AB = EI(N)
    dp = [[-1]*(H+1) for _ in range(N+1)]
    dp[0][H] = M
    for i in range(N):
        a, b = AB[i]
        for j in range(H+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]-b)
            if j+a <= H:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j+a])
    # print(*dp, sep="\n")
    for i in range(N, -1, -1):
        if max(dp[i]) != -1:
            print(i)
            return


if __name__ == "__main__":
    main()
