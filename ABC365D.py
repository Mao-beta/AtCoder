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
    N = NI()
    S = SI()
    # i回終わって、最後がjのときのmax
    INF = 10**10
    dp = [[-INF]*3 for _ in range(N+1)]
    if S[0] == "R":
        dp[1][0] = 0
        dp[1][1] = 1
    elif S[0] == "P":
        dp[1][1] = 0
        dp[1][2] = 1
    else:
        dp[1][2] = 0
        dp[1][0] = 1

    for i in range(1, N):
        s = S[i]
        s = "RPS".index(s)
        for j in range(3):
            for nj in range(3):
                if j == nj or (s-nj)%3 == 1:
                    continue
                dp[i+1][nj] = max(dp[i+1][nj], dp[i][j] + int((nj-s)%3 == 1))

    print(max(dp[-1]))


if __name__ == "__main__":
    main()
