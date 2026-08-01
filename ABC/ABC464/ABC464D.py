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
    T = NI()
    for _ in range(T):
        N = NI()
        S = [int(s == "R") for s in SI()]
        X = NLI()
        Y = NLI()
        INF = 10**18
        dp = [[-INF]*2 for _ in range(N+1)]
        dp[1][0] = 0 if S[0] == 0 else -X[0]
        dp[1][1] = 0 if S[0] == 1 else -X[0]
        for i in range(2, N+1):
            for j in range(2):
                for nj in range(2):
                    c = 0
                    if S[i-1] != nj:
                        c -= X[i-1]
                    if j == 1 and nj == 0:
                        c += Y[i-2]
                    dp[i][nj] = max(dp[i][nj], dp[i-1][j] + c)
        # print(S, X, Y)
        # print(*dp, sep="\n")
        print(max(dp[N]))


if __name__ == "__main__":
    main()
