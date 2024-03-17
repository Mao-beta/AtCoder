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
    A = NLI()
    INF = 10**20
    E = [[[INF]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
    C = [0] * 3
    for a in A:
        if a >= 3:
            continue
        C[a] += 1
    E[0][0][0] = 0
    for n0 in range(N+1):
        for n1 in range(N+1-n0):
            for n2 in range(N+1-n0-n1):
                if n0 == n1 == n2 == 0:
                    continue
                e = 1
                if n0 > 0:
                    e += E[n0-1][n1+1][n2] * n0 / N
                if n1 > 0:
                    e += E[n0][n1-1][n2+1] * n1 / N
                if n2 > 0:
                    e += E[n0][n1][n2-1] * n2 / N
                a = (N-n0-n1-n2) / N
                E[n0][n1][n2] = e / (1-a)

    print(E[C[0]][C[1]][C[2]])


if __name__ == "__main__":
    main()
