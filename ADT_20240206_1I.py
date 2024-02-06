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
    N, X, Y = NMI()
    A = NLI()
    B = NLI()
    INF = 10**20
    dp = [INF] * (1<<N)
    dp[0] = 0
    for i in range((1<<N)-1):
        b = B[bin(i).count("1")]
        r = 0
        for j in range(N):
            if (i>>j) & 1:
                continue
            ni = i | (1<<j)
            cost = r * Y + abs(A[j]-b) * X
            dp[ni] = min(dp[ni], dp[i] + cost)
            r += 1
    print(dp[-1])


if __name__ == "__main__":
    main()
