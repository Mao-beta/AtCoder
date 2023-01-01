import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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
    N, X = NMI()
    A = NLI()
    M = 10000
    G = [set() for _ in range(M+1)]
    for i in range(M+1):
        for p in permutations(str(i)):
            G[i].add(int("".join(p)))

    INF = 1000
    dp = [-INF] * (M+1)
    dp[X] = 0

    for i in range(N):
        a = A[i]
        dp2 = [-INF] * (M+1)
        for x in range(M+1):
            for g in G[x]:
                dp2[g] = max(dp2[g], dp[x])
                if g >= a:
                    dp2[g-a] = max(dp2[g-a], dp[x] + 1)
        dp = dp2

    print(max(dp))


if __name__ == "__main__":
    main()
