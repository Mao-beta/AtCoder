import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    A = NLI()
    if N == 1:
        print(0)
        return
    INF = 10**18

    # C[g]: g日平日のあと1日休みのときの総和
    C = [0] * N
    for g in range(1, N):
        m = (g+1)//2
        C[g] = sum(A[:m]) * 2
        if g % 2:
            C[g] -= A[m-1]

    dp = [-INF] * (N+1)
    dp[0] = 0
    for i in range(N-1):
        for j in range(i+1, N+1):
            g = j-i
            dp[j] = max(dp[j], dp[i] + C[g-1])

    print(dp[N])


if __name__ == "__main__":
    main()
