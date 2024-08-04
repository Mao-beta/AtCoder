import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N, X, Y = NMI()
    AB = EI(N)
    INF = 10**9
    dp = [[INF]*(X+1) for _ in range(N+1)]
    dp[0][0] = 0
    ans = 0
    for a, b in AB:
        for n in range(N-1, -1, -1):
            for x in range(X, -1, -1):
                if dp[n][x] > Y:
                    continue
                # print(a, b, n, x, dp[n][x])
                if x+a <= X:
                    dp[n+1][x+a] = min(dp[n+1][x+a], dp[n][x]+b)
    for n in range(N, -1, -1):
        for x in range(X, -1, -1):
            if dp[n][x] >= INF:
                continue
            if dp[n][x] <= Y:
                if n < N:
                    ans = max(ans, n+1)
                else:
                    ans = n
            else:
                ans = max(ans, n)

    print(ans)


if __name__ == "__main__":
    main()
