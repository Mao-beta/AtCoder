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
    N, M, H, K = NMI()
    S = SI()
    XY = set()
    for _ in range(M):
        XY.add(tuple(NMI()))

    DIR = {s: tup for s, tup in zip("RLUD",
                                    [(1, 0), (-1, 0), (0, 1), (0, -1)])}

    nx, ny = 0, 0
    for s in S:
        dx, dy = DIR[s]
        nx += dx
        ny += dy
        H -= 1
        if H < 0:
            print("No")
            return

        if H < K and (nx, ny) in XY:
            H = K
            XY.discard((nx, ny))

    print("Yes")


if __name__ == "__main__":
    main()
