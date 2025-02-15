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
EI = lambda m: [NLI() for _ in range(m)]


def main(N):
    L = len(N)
    # dp[less][i][j]: 上からi桁みて、末尾の状態がj(0:以外、1:4、2:40)
    dp = [[[0]*3 for _ in range(L+1)] for _ in range(2)]
    dp[0][0][0] = 1
    for i, n in enumerate(N):
        n = int(n)
        for j in range(3):
            for less in range(2):
                xmax = 9 if less else n
                for x in range(xmax+1):
                    ni = i+1
                    if x == 4:
                        if j == 2:
                            continue
                        nj = 1
                    elif j == 1 and x == 0:
                        nj = 2
                    else:
                        nj = 0

                    if not less and x == xmax:
                        nless = 0
                    else:
                        nless = 1

                    dp[nless][ni][nj] += dp[less][i][j]
                    dp[nless][ni][nj] %= MOD99
    ans = -1
    for less in range(2):
        for j in range(3):
            # print(less, L, j, dp[less][L][j])
            ans += dp[less][L][j]
    return ans % MOD99


def guchoku(N):
    ans = 0
    for n in range(1, int(N)+1):
        n = str(n)
        if "404" not in n:
            ans += 1
    return ans % MOD99


if __name__ == "__main__":
    N = SI()
    print(main(N))
    exit()
    for N in range(1, 10**6):
        N = str(N)
        ans = main(N)
        gu = guchoku(N)
        assert ans == gu, (N, ans, gu)