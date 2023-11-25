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
    D = [[0]*N for _ in range(N)]
    for i in range(N-1):
        DD = NLI()
        for j in range(i+1, N):
            d = DD[j-i-1]
            D[i][j] = d
            D[j][i] = d

    # dp[case]: 選んだ頂点集合がcase
    dp = [0] * (1<<N)
    for case in range(1<<N):
        for i in range(N):
            for j in range(i+1, N):
                if (case >> i) & 1 or (case >> j) & 1:
                    continue
                goto = case | (1<<i) | (1<<j)
                dp[goto] = max(dp[goto], dp[case] + D[i][j])

    print(max(dp))


if __name__ == "__main__":
    main()
