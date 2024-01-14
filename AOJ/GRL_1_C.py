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
    N, M = NMI()
    STD = EI(M)

    INF = 10**15
    D = [[INF]*N for _ in range(N)]
    for i in range(N):
        D[i][i] = 0
    for s, t, d in STD:
        D[s][t] = d

    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

    D2 = [d[:] for d in D]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D2[i][j] = min(D2[i][j], D2[i][k] + D2[k][j])

    if D == D2:
        for row in D:
            row = ["INF" if d >= 10**13 else d for d in row]
            print(*row)

    else:
        print("NEGATIVE CYCLE")


if __name__ == "__main__":
    main()
