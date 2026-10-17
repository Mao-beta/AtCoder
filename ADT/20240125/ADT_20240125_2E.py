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
    C = EI(3)
    res = 0
    for P in permutations(range(9)):
        X = [[] for _ in range(8)]
        for p in P:
            h, w = divmod(p, 3)
            c = C[h][w]

            if p in [0, 1, 2]:
                X[0].append(c)
            if p in [3, 4, 5]:
                X[1].append(c)
            if p in [6, 7, 8]:
                X[2].append(c)
            if p in [0, 3, 6]:
                X[3].append(c)
            if p in [1, 4, 7]:
                X[4].append(c)
            if p in [2, 5, 8]:
                X[5].append(c)
            if p in [0, 4, 8]:
                X[6].append(c)
            if p in [2, 4, 6]:
                X[7].append(c)
        ok = True
        for t in range(8):
            if X[t][0] == X[t][1] and X[t][0] != X[t][2]:
                ok = False
        res += int(ok)

    print(res / math.factorial(9))


if __name__ == "__main__":
    main()
