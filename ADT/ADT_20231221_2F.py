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
    S = [SI() for _ in range(9)]
    P = set()
    for h in range(9):
        for w in range(9):
            if S[h][w] == "#":
                P.add((h, w))

    def is_square(Ps):
        L = []
        for X, Y in combinations(Ps, 2):
            l = (X[0]-Y[0]) ** 2 + (X[1]-Y[1])**2
            L.append(l)
        L.sort()
        a, b, c, d, e, f = L
        return a*2 == b*2 == c*2 == d*2 == e == f and a > 0

    ans = 0
    for Ps in combinations(P, 4):
        ans += int(is_square(Ps))
    print(ans)


if __name__ == "__main__":
    main()
