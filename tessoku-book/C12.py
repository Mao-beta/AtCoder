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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S), start=1):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N, M, K = NMI()
    AB = [NLI() for _ in range(M)]

    # i+1以上j以下を同じ章にしたときの良さ
    C = [[0]*(N+1) for _ in range(N+1)]
    for a, b in AB:
        for i in range(a):
            for j in range(b, N+1):
                C[i][j] += 1

    # i個まで見てj個に分割したときのMax
    INF = 10**10
    dp = [[-INF]*(K+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(K):
            if dp[i][j] < 0: continue
            for ni in range(i+1, N+1):
                dp[ni][j+1] = max(dp[ni][j+1], dp[i][j] + C[i][ni])

    ans = dp[-1][K]
    print(max(0, ans))


if __name__ == "__main__":
    main()
