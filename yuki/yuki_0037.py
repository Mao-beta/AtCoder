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
    T = NI()
    N = NI()
    C = NLI()
    V = NLI()
    CV = []
    for c, v in zip(C, V):
        while v > 0:
            CV.append([c, v])
            v //= 2
    N = len(CV)
    dp = [[0]*(T+1) for _ in range(N+1)]
    for i in range(N):
        c, v = CV[i]
        for j in range(T+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j+c <= T:
                dp[i+1][j+c] = max(dp[i+1][j+c], dp[i][j]+v)
    print(max(dp[-1]))


if __name__ == "__main__":
    main()
