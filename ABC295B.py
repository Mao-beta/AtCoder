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
    H, W = NMI()
    B = [list(SI()) for _ in range(H)]

    for h in range(H):
        for w in range(W):
            x = B[h][w]
            if x == "." or x == "#":
                continue
            x = int(x)
            for bh in range(H):
                for bw in range(W):
                    if abs(bh-h) + abs(bw-w) <= x and B[bh][bw] == "#":
                        B[bh][bw] = "."
            B[h][w] = "."

    for row in B:
        print("".join(row))



if __name__ == "__main__":
    main()
