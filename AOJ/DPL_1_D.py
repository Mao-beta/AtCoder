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
    N = NI()
    A = [NI() for _ in range(N)]
    INF = 10**20
    dp = [INF] * N
    for a in A:
        idx = bisect.bisect_left(dp, a)
        dp[idx] = a
    print(bisect.bisect_left(dp, INF))


if __name__ == "__main__":
    main()
