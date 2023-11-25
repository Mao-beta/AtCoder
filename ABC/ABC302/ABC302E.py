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
    N, Q = NMI()
    D = [0] * N
    S = [set() for _ in range(N)]
    Z = N

    for _ in range(Q):
        q, *X = NMI()
        if q == 1:
            u, v = X
            u -= 1
            v -= 1
            if D[u] == 0:
                Z -= 1
            if D[v] == 0:
                Z -= 1
            S[u].add(v)
            S[v].add(u)
            D[u] += 1
            D[v] += 1
        else:
            v = X[0] - 1
            if D[v] > 0:
                Z += 1
            D[v] = 0

            for s in list(S[v]):
                D[s] -= 1
                if D[s] == 0:
                    Z += 1
                S[s].discard(v)

            S[v] = set()
        print(Z)



if __name__ == "__main__":
    main()
