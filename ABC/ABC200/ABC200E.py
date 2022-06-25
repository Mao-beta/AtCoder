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
    N, K = NMI()
    F = [0] * (3*N+5)
    F[3] = 1
    F[N+3] = -3
    F[N*2+3] = 3
    F[N*3+3] = -1
    for i in range(4):
        F = list(accumulate(F))

    pqr = bisect.bisect_left(F, K)
    K -= F[pqr-1]

    G = [0] * (3*N+5)
    G[2] = 1
    G[N+2] = -2
    G[N*2+2] = 1
    for i in range(2):
        G = list(accumulate(G))

    p = 0
    for p in range(1, pqr):
        x = G[pqr-p]
        if K > x:
            K -= x
        else:
            break

    qr = pqr - p
    # print(p, qr, K)
    for q in range(1, N+1):
        r = qr - q
        if not 1 <= r <= N:
            continue
        K -= 1
        if K == 0:
            print(p, q, r)
            exit()


if __name__ == "__main__":
    main()
