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
    N, K = NMI()
    A = NLI()
    dp = [0] * (N+1)
    for i in range(N+1):
        res = 0
        for a in A:
            if i-a >= 0:
                if dp[i-a] == 0:
                    res = 1
        dp[i] = res
    if dp[N]:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
