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


def print_err(*args):
    print(*args, file=sys.stderr)


def main():
    N = NI()
    A = NLI()
    S = [SI() for _ in range(N)]
    Q = NI()
    UV = EI(Q)

    INF = 10 ** 18
    M = 10 ** 14
    D = [[INF]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if S[i][j] == "Y":
                D[i][j] = M - A[j]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

    for u, v in UV:
        u, v = u-1, v-1
        val = D[u][v]
        if val >= INF:
            print("Impossible")
        else:
            d = (val + M - 1) // M
            c = (-val) % M + A[u]
            print(d, c)



if __name__ == "__main__":
    main()
