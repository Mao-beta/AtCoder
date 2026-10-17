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


def main():
    H, W, N = NMI()
    A = [NLI() for _ in range(H)]
    C = [0] + NLI()
    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    for h in range(H):
        for w in range(W):
            a = A[h][w]
            for dh, dw in zip(DH, DW):
                nh, nw = h+dh, w+dw
                if 0 <= nh < H and 0 <= nw < W:
                    na = A[nh][nw]
                    if a != na and C[a] == C[na]:
                        print("No")
                        exit()

    print("Yes")


if __name__ == "__main__":
    main()
