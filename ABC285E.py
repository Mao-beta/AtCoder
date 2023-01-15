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


def print_err(*args):
    print(*args, file=sys.stderr)


def main():
    N = NI()
    A = NLI()

    S = list(accumulate([0]+A))
    GA = [0]
    for i in range(1, N+1):
        if i % 2:
            GA.append(S[i//2] + S[i//2+1])
        else:
            GA.append(S[i//2]*2)

    INF = 10**15
    dp = [[-INF]*(N+1) for _ in range(N+1)]
    dp[1][0] = GA[N-1]

    for i in range(1, N):
        for j in range(i):
            gap = N - (i-j)
            if dp[i][j] < 0:
                continue

            # 休日にする
            dp[i+1][0] = max(dp[i+1][0], dp[i][j] - GA[gap] + GA[j] + GA[N-1-i])
            # しない
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])

    print(max(dp[N]))


if __name__ == "__main__":
    main()
