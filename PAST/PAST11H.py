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
    WV = [NLI() for _ in range(N)]
    dp = [[[0]*(B+1) for _ in range(A+1)] for _ in range(N+1)]

    for i, (w, v) in enumerate(WV):
        for a in range(A+1):
            for b in range(B+1):
                d = dp[i][a][b]
                dp[i+1][a][b] = max(dp[i+1][a][b], d)
                if a + w <= A:
                    dp[i+1][a+w][b] = max(dp[i+1][a+w][b], d + v)
                if b + w <= B:
                    dp[i+1][a][b+w] = max(dp[i+1][a][b+w], d + v)

    ans = 0
    for a in range(A + 1):
        for b in range(B + 1):
            ans = max(ans, dp[-1][a][b])
    print(ans)


if __name__ == "__main__":
    main()
