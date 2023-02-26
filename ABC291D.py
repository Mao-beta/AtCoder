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
    N = NI()
    AB = EI(N)

    dp = [[0]*2 for _ in range(N+1)]
    dp[1][0] = 1
    dp[1][1] = 1

    for i in range(1, N):
        for j in range(2):
            for pj in range(2):
                if AB[i][j] == AB[i-1][pj]:
                    continue
                dp[i+1][j] += dp[i][pj]
                dp[i+1][j] %= MOD99

    print(sum(dp[-1]) % MOD99)


if __name__ == "__main__":
    main()
