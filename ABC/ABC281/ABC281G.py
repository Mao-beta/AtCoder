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
    N, M = NMI()

    # P2[i]: pow(2, i, M)
    P2 = [1]
    for i in range(N**2+5):
        P2.append(P2[-1] * 2 % M)

    # P2JX[j][x]: pow((P2[j]-1), x, M)
    P2JX = [[pow((P2[j]-1), x, M) for x in range(N)] for j in range(N+1)]

    # nCr % M
    com = [[0]*(N+1) for _ in range(N+1)]
    com[0][0] = 1
    for n in range(N):
        for r in range(N):
            c = com[n][r]
            com[n+1][r] += c
            com[n+1][r] %= M
            com[n+1][r+1] += c
            com[n+1][r+1] %= M

    # dp[i][j]:
    # それまで使った頂点がi個で、(1<=i<N+1)
    # 距離最大の頂点数がj個のときの場合の数(1<=j<N)
    dp = [[0]*N for _ in range(N)]
    # 頂点1は距離0で1個のみ
    dp[1][1] = 1
    for i in range(1, N):
        for j in range(1, N):
            d = dp[i][j]
            if d == 0:
                continue
            for x in range(1, N-i):
                ni = i+x
                nj = x
                a = P2JX[j][x] * P2[x*(x-1)//2] % M * com[N-1-i][x] % M
                dp[ni][nj] += a * d
                dp[ni][nj] %= M

    ans = 0
    for j in range(N):
        d = dp[N-1][j]
        ans += (P2[j]-1) * d
        ans %= M

    print(ans)


if __name__ == "__main__":
    main()
