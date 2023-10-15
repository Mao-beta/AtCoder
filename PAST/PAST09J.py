import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

import numpy as np

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
    G = np.array([[0]*N for _ in range(N)])
    # 通常 0, 90, 180, 270
    # 左右反転 0, 90, 180, 270
    RotA = [1, 2, 3, 0, 5, 6, 7, 4]
    RotB = [3, 0, 1, 2, 7, 4, 5, 6]
    RevLR = [4, 7, 6, 5, 0, 3, 2, 1]
    RevUD = [6, 5, 4, 7, 2, 1, 0, 3]
    now = 0
    for _ in range(Q):
        q, *X = SMI()
        match q:
            case "1":
                x, y = X
                x, y = int(x)-1, int(y)-1
                G[x][y] ^= 1

            case "2":
                c = X[0]
                if c == "A":
                    G = np.rot90(G, -1)
                else:
                    G = np.rot90(G, 1)

            case "3":
                c = X[0]
                if c == "A":
                    G = np.flipud(G)
                else:
                    G = np.fliplr(G)

    G = G.tolist()
    for row in G:
        print("".join(map(str, row)))


if __name__ == "__main__":
    main()
