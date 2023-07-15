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
    P = []
    C = []
    F = []
    for _ in range(N):
        p, c, *Fi = NMI()
        P.append(p)
        C.append(c)
        F.append(set(Fi))

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if P[i] < P[j]:
                continue
            if len(F[i] - F[j]) > 0:
                continue
            if P[i] > P[j]:
                print("Yes")
                exit()
            if P[i] == P[j] and len(F[j] - F[i]) >= 1:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
