import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache

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



# 約数列挙（単体）
def divisors(x):
    res = set()
    for i in range(1, int(x**0.5) + 2):
        if x % i == 0:
            res.add(i)
            res.add(x//i)
    return res


def main():
    # input
    N, X = NMI()
    LA = [NLI() for _ in range(N)]

    dp = [defaultdict(int) for _ in range(N+1)]
    dp[0][1] = 1

    for i, (L, *A) in enumerate(LA):
        C = Counter(A)
        for key, val in C.items():
            for j in dp[i].keys():
                nj = key * j
                dp[i+1][nj] += dp[i][j] * val

    print(dp[N][X])


if __name__ == "__main__":
    main()
