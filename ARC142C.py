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


def ask(u, v):
    print(f"? {u} {v}")
    sys.stdout.flush()


def answer(d):
    print(f"! {d}")
    sys.stdout.flush()
    exit()


def main():
    N = NI()
    D1 = [0] * (N+1)
    D2 = [0] * (N+1)
    P = [0] * (N+1)
    G = [0] * (N+1)

    for v in range(3, N+1):
        ask(1, v)
        d = NI()
        D1[v] = d

        ask(2, v)
        d = NI()
        D2[v] = d

        P[v] = D1[v] + D2[v]
        G[v] = D1[v] - D2[v]

    M = 0
    S = 200
    for v in range(3, N+1):
        M = max(abs(D1[v] - D2[v]), M)
        S = min(D1[v] + D2[v], S)

    CP = Counter(P)
    CG = Counter(G)
    CP[0] -= 3
    CG[0] -= 3
    # print(M, S)
    # print(P)
    # print(G)

    if CG[0] > 0:
        answer(S)

    for d in range(1, 200):
        if CP[d] != d-1:
            continue

        if d == 1:
            if CG[-1] + CG[1] != N-2:
                continue

        answer(d)


if __name__ == "__main__":
    main()
