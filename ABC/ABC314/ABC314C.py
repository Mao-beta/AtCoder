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
    S = list(SI())
    T = [""] * N
    C = NLI()
    P = [[] for _ in range(M+1)]
    for i, (s, c) in enumerate(zip(S, C)):
        P[c].append(i)
    # print(P)
    for m in range(1, M+1):
        if len(P[m]) == 1:
            T[P[m][0]] = S[P[m][0]]
        for j in range(len(P[m])):
            nj = (j+1) % len(P[m])
            T[P[m][nj]] = S[P[m][j]]
        # print("".join(S))

    print("".join(T))


if __name__ == "__main__":
    main()
