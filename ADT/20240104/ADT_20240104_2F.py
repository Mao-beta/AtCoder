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
    N, M = NMI()
    AB = EI(M)
    CD = EI(M)
    AB.sort()
    for P in permutations(range(N)):
        XY = []
        for c, d in CD:
            x, y = P[c-1]+1, P[d-1]+1
            XY.append(sorted([x, y]))
        XY.sort()
        if XY == AB:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
