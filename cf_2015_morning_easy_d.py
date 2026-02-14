import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    S = SI()
    ans = N
    for i in range(N+1):
        X = S[:i]
        Y = S[i:]

        def edit_distance(S, T):
            N = len(S)
            M = len(T)

            INF = N + M + 2
            dp = [[INF] * (M + 1) for _ in range(N + 1)]
            for i in range(N + 1):
                dp[i][-1] = N - i
            for j in range(M + 1):
                dp[-1][j] = M - j

            for i in range(N - 1, -1, -1):
                s = S[i]
                for j in range(M - 1, -1, -1):
                    t = T[j]

                    dp[i][j] = min(
                        dp[i + 1][j] + 1, dp[i][j + 1] + 1
                    )
                    if s == t:
                        dp[i][j] = min(dp[i][j], dp[i+1][j+1])

            return dp[0][0]

        ans = min(ans, edit_distance(X, Y))
    print(ans)


if __name__ == "__main__":
    main()
