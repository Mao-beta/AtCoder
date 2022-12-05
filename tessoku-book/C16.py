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
    N, M, K = NMI()
    ASBT = EI(M)
    dp = [0] * N
    events = [[s, a-1, b-1, t] for a, s, b, t in ASBT]
    heapify(events)
    while events:
        now, a, b, t = heappop(events)
        if a >= 0:
            heappush(events, [t+K, ~b, dp[a], None])
        else:
            dp[~a] = max(dp[~a], b+1)
    print(max(dp))


if __name__ == "__main__":
    main()
