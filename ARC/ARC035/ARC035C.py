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


def main():
    N, M = NMI()
    ABC = [NLI() for _ in range(M)]
    K = NI()
    XYZ = [NLI() for _ in range(K)]

    INF = 10**10
    D = [[INF]*N for _ in range(N)]

    for a, b, c in ABC:
        a, b = a-1, b-1
        a, b = min(a, b), max(a, b)
        D[a][b] = c
        D[b][a] = c

    for i in range(N):
        D[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

    # print(*D, sep="\n")

    for x, y, z in XYZ:
        x, y = x-1, y-1

        ans = 0
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][x] + D[y][j] + z, D[i][y] + D[x][j] + z)
                ans += D[i][j]

        # print(*D, sep="\n")
        print(ans // 2)


if __name__ == "__main__":
    main()
