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
    N = NI()
    D = NLI()
    dp = [[0]*18 for _ in range(1<<N)]
    dp[0][1] = 100
    for case in range(1<<N):
        for lv in range(17):
            for i in range(N):
                if dp[case][lv] <= 0:
                    continue
                if (case >> i) & 1:
                    continue
                if D[i] > 0:
                    dp[case | (1<<i)][lv] = max(dp[case | (1<<i)][lv], min(100*lv, dp[case][lv] + D[i]))
                else:
                    dp[case | (1<<i)][lv+1] = max(dp[case | (1<<i)][lv+1], max(0, dp[case][lv] + D[i]))

    print(max(dp[-1]))


if __name__ == "__main__":
    main()
