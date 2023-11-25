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
    N, M, H, K = NMI()
    S = SI()
    XY = set(tuple(NMI()) for _ in range(M))
    nx, ny = 0, 0
    D = {
        "R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)
    }
    k = H
    for s in S:
        dx, dy = D[s]
        nx += dx
        ny += dy
        k -= 1
        if 0 <= k < K and (nx, ny) in XY:
            XY.discard((nx, ny))
            k = K
        elif k < 0:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
