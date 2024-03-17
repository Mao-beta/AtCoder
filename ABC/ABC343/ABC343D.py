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
    N, T = NMI()
    AB = EI(T)
    AB = [[x-1, y] for x, y in AB]
    S = set()
    S.add(0)
    C = Counter()
    C[0] = N
    X = [0] * N
    for a, b in AB:
        p = X[a]
        X[a] += b
        C[p] -= 1
        if C[p] == 0:
            S.discard(p)
        C[X[a]] += 1
        S.add(X[a])
        print(len(S))


if __name__ == "__main__":
    main()
