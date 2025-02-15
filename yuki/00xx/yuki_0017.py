import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    S = [NI() for _ in range(N)]
    M = NI()
    ABC = EI(M)
    INF = 10**10
    D = [[INF]*N for _ in range(N)]
    for i in range(N):
        D[i][i] = 0
    for a, b, c in ABC:
        D[a][b] = c
        D[b][a] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    ans = INF
    for i in range(1, N-1):
        for j in range(1, N-1):
            if i == j:
                continue
            ans = min(ans, D[0][i] + D[i][j] + D[j][N-1] + S[i] + S[j])

    print(ans)


if __name__ == "__main__":
    main()
