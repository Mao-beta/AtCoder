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
    N, M, L = NMI()
    A = NLI()
    INF = 10**10
    dp = [[INF] * M for _ in range(L+1)]
    dp[0][0] = 0
    for i in range(L):
        for j in range(M):
            for t in range(M):
                add = 0
                for k in range(i, N, L):
                    add += (t - A[k]) % M
                dp[i+1][(j+t)%M] = min(dp[i+1][(j+t)%M], dp[i][j] + add)
                    
    # print(*dp, sep="\n")
    print(dp[L][0])


if __name__ == "__main__":
    main()
