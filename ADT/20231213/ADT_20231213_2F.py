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
    total = 0
    for P in permutations(range(9)):
        SameH = [[] for _ in range(3)]
        SameW = [[] for _ in range(3)]
        Cross = [[] for _ in range(2)]
        for p in P:
            h, w = divmod(p, 3)
            p = (h, w)
            SameH[h].append(p)
            SameW[w].append(p)
            if p in [(0, 0), (1, 1), (2, 2)]:
                Cross[0].append(p)
            if p in [(0, 2), (1, 1), (2, 0)]:
                Cross[1].append(p)
        ok = True
        for row in SameH + SameW + Cross:
            if C[row[0][0]][row[0][1]] == C[row[1][0]][row[1][1]]:
                ok = False
        if ok:
            res += 1
        total += 1
    print(res / total)


if __name__ == "__main__":
    main()
