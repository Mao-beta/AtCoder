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
    N, A, B = NMI()
    dp = [0] * (N+1)
    for i in range(N+1):
        a, b = 1, 1
        if i - A >= 0:
            a = dp[i-A]
        if i - B >= 0:
            b = dp[i-B]
        
        if a & b == 0:
            dp[i] = 1

    # print(dp)

    if dp[N]:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
