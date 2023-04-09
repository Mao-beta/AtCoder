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
    N, K = NMI()
    A = EI(N)
    Q = NI()
    ST = EI(Q)
    ST = [[x-1, y-1] for x, y in ST]

    INF = 10**20

    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                A[i][j] = INF

    for k in range(N):
        for i in range(N):
            for j in range(N):
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])

    for s, t in ST:
        s %= N
        t %= N
        ans = A[s][t]
        print(ans if ans < INF else -1)


if __name__ == "__main__":
    main()
