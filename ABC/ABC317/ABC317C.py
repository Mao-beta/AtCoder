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
    N, M = NMI()
    ABC = EI(M)
    INF = 10**20
    D = [[INF]*N for _ in range(N)]
    for a, b, c in ABC:
        a, b = a-1, b-1
        D[a][b] = c
        D[b][a] = c

    dp = [[-1] * N for _ in range(1<<N)]
    for i in range(N):
        dp[1<<i][i] = 0

    for case in range(1<<N):
        for now in range(N):
            if dp[case][now] < 0:
                continue
            for goto in range(N):
                if (case >> goto) & 1:
                    continue
                if D[now][goto] >= INF:
                    continue
                dp[case | (1<<goto)][goto] = max(dp[case | (1<<goto)][goto], dp[case][now] + D[now][goto])

    ans = 0
    for case in range(1<<N):
        for now in range(N):
            ans = max(ans, dp[case][now])

    print(ans)


if __name__ == "__main__":
    main()
