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
    N, M = NMI()
    C = []
    P = []
    S = [[] for _ in range(N)]
    Z = [0] * N
    for i in range(N):
        c, p, *s = NMI()
        C.append(c)
        P.append(p)
        Z[i] = s.count(0)
        for ss in s:
            if ss != 0:
                S[i].append(ss)

    E = [0] * (M+105)
    INF = 10**10
    for x in range(M-1, -1, -1):
        cost = INF
        for c, p, s, z in zip(C, P, S, Z):
            esum = 0
            for ss in s:
                esum += E[x+ss]
            tmp = (esum + p * c) / (p-z)
            cost = min(cost, tmp)
        E[x] = cost
    print(E[0])


if __name__ == "__main__":
    main()
