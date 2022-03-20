import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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
    K = NI()
    N = 1 << K
    R = [NI() for _ in range(N)]

    # W[i][j]: iがjに勝つ確率
    W = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ri = R[i]
            rj = R[j]
            p = 1 / (1 + pow(10, (rj - ri)/400))
            W[i][j] = p

    # iがk連勝する確率　各dp[i][K]が答え
    dp = [[0]*(K+1) for _ in range(N)]
    for i in range(N):
        dp[i][0] = 1

    for k in range(K):
        for i in range(N):
            start = ((i>>k)^1) << k
            m = 1 << k
            for j in range(start, start+m):
                dp[i][k+1] += W[i][j] * dp[j][k] * dp[i][k]

    # print(*dp, sep="\n")

    for i in range(N):
        print(dp[i][K])


if __name__ == "__main__":
    main()
