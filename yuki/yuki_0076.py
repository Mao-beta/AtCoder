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
    T = NI()
    M = 10**6
    E = [0.0] * (M+7)
    E[M-1] = 1.0000000000000000
    E[M-2] = 1.0833333333333333
    E[M-3] = 1.2569444444444444
    E[M-4] = 1.5353009259259260
    E[M-5] = 1.6915991512345676
    E[M-6] = 2.0513639724794235

    P = [0.0] * 7
    for i in range(2, 7):
        # P[i-1]を順に求める
        # E[M-i] = 1 + E[M-i+1]*P[1] + E[M-i+2]*P[2] * ...
        e = E[M-i]-1
        a = E[M-1]
        for x in range(1, i-1):
            e -= E[M-i+x] * P[x]
        P[i-1] = e / a
    P[6] = 1-sum(P)
    # print(P)

    for i in range(M-7, -1, -1):
        E[i] = 1
        for x in range(1, 7):
            E[i] += P[x] * E[i+x]
    for _ in range(T):
        N = NI()
        print(E[M-N])


if __name__ == "__main__":
    main()
