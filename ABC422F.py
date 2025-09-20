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
    N, M = NMI()
    W = NLI()
    UV = EI(M)
    UV = [[x-1, y-1] for x, y in UV]
    # dp(頂点、あと何回移動するか)=そこからの消費燃料
    INF = 10**20
    dp = [INF] * N
    dp[0] = 0
    for j in range(M, 0, -1):
        dp2 = [INF] * N
        dp2[0] = 0
        for u, v in UV:
            dp2[v] = min(dp2[v], dp[u] + j * W[u])
            dp2[u] = min(dp2[u], dp[v] + j * W[v])
        dp, dp2 = dp2, dp
    dp[0] = 0
    print(*dp, sep='\n')


if __name__ == "__main__":
    main()
