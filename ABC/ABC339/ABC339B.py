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
    H, W, N = NMI()
    S = [["."]*W for _ in range(H)]
    # URDL
    DH = [-1, 0, 1, 0]
    DW = [0, 1, 0, -1]
    d = 0
    h, w = 0, 0
    for _ in range(N):
        if S[h][w] == ".":
            S[h][w] = "#"
            d += 1
        else:
            S[h][w] = "."
            d -= 1
        d %= 4
        h, w = h + DH[d], w + DW[d]
        h %= H
        w %= W

    for row in S:
        print("".join(row))



if __name__ == "__main__":
    main()
