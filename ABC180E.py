import sys
import math
from collections import deque
from functools import lru_cache


sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def Salesman(dist, need_return):
    N = len(dist)
    INF = 10**20
    dp = [[INF]*(1<<N) for _ in range(N)]
    dp[0][1] = 0

    for S in range(1<<N):
        for i in range(N):
            if dp[i][S] == INF: continue
            for k in range(1, N):
                if (S>>k) & 1 == 0:
                    dp[k][S + 2**k] = min(dp[i][S] + dist[i][k], dp[k][S + 2**k])

    ans = INF
    for i in range(1, N):
        if need_return:
            ans = min(dp[i][(1<<N)-1] + dist[i][0], ans)
        else:
            ans = min(dp[i][(1 << N) - 1], ans)
    return ans


def main():
    N = NI()
    P = [NLI() for _ in range(N)]
    dist = [[10**20]*N for _ in range(N)]
    for i, p in enumerate(P):
        for j, q in enumerate(P):
            cost = abs(p[0] - q[0]) + abs(p[1] - q[1]) + max(0, q[2] - p[2])
            dist[i][j] = cost

    print(Salesman(dist, True))


if __name__ == "__main__":
    main()
