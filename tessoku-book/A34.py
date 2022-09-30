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


def main():
    N, X, Y = NMI()
    A = NLI()
    dp = [0] * (10**5 + 1)
    
    for i in range(10**5 + 1):
        G = set()
        if i - X >= 0:
            G.add(dp[i - X])
        if i - Y >= 0:
            G.add(dp[i - Y])

        for g in range(5):
            if g not in G:
                dp[i] = g
                break
    
    x = 0
    for a in A:
        x ^= dp[a]

    if x:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
