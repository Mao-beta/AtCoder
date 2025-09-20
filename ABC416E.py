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
    ABC = EI(M)
    ABC = [[x-1, y-1, w] for x, y, w in ABC]
    K, T = NMI()
    D = NLI()
    D = [x-1 for x in D]
    Q = NI()
    querys = EI(Q)
    INF = 10**18
    ans = 0
    # Nは空港
    F = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(N):
        F[i][i] = 0
    for d in D:
        F[d][N] = min(F[d][N], T)
        F[N][d] = min(F[N][d], 0)
    for a, b, c in ABC:
        F[a][b] = min(F[a][b], c)
        F[b][a] = min(F[b][a], c)
    for k in range(N+1):
        for i in range(N+1):
            for j in range(N+1):
                F[i][j] = min(F[i][j], F[i][k] + F[k][j])
    for i in range(N):
        for j in range(N):
            if F[i][j] < INF:
                ans += F[i][j]
    # print(*F, sep="\n")
    # print(ans)

    for q, *X in querys:
        # print(q, X)
        if q == 1:
            x, y, t = X
            x, y = x-1, y-1
            F[x][y] = min(F[x][y], t)
            F[y][x] = min(F[y][x], t)
            for k in (x, y):
                for i in range(N+1):
                    for j in range(N+1):
                        F[i][j] = min(F[i][j], F[i][k] + F[k][j])

        elif q == 2:
            x = X[0]-1
            y = N
            F[x][y] = min(F[x][y], T)
            F[y][x] = min(F[y][x], 0)
            for k in (x, y):
                for i in range(N + 1):
                    for j in range(N + 1):
                        F[i][j] = min(F[i][j], F[i][k] + F[k][j])

        else:
            ans = 0
            for i in range(N):
                for j in range(N):
                    if F[i][j] < INF:
                        ans += F[i][j]
            print(ans)

        # print(*F, sep="\n")


if __name__ == "__main__":
    main()
