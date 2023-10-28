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


def main():
    N = NI()
    D = NLI()
    L1, C1, K1 = NMI()
    L2, C2, K2 = NMI()
    # i個見て、センサー1をj個使ったときのセンサー2の個数の最小値
    INF = 10**18
    dp = [[INF]*(K1+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        d = D[i]
        for j in range(K1+1):
            rem = K1 - j
            for k in range(rem+1):
                rd = max(0, d - L1*k)
                num = (rd + L2-1) // L2
                nk = dp[i][j] + num
                if nk <= K2:
                    dp[i+1][j+k] = min(dp[i+1][j+k], nk)

    ans = INF
    for j in range(K1+1):
        ans = min(ans, j * C1 + dp[-1][j] * C2)
    if ans >= INF:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
