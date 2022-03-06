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
    N, X = NMI()
    AB = [NLI() for _ in range(N)]
    dp = [[0] * 10101 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        a, b = AB[i]
        for j in range(10001):
            dp[i+1][j+a] |= dp[i][j]
            dp[i+1][j+b] |= dp[i][j]

    # print(dp)
    if dp[-1][X]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
