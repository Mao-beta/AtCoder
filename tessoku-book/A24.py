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
    A = NLI()

    INF = 10**10
    dp = [INF] * (N+2)
    # i個のLISの最小
    dp[0] = 0
    for a in A:
        idx = bisect.bisect_left(dp, a)
        dp[idx] = a

    print(dp.index(INF)-1)


if __name__ == "__main__":
    main()
