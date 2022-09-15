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
    H, W = NMI()
    S = [list(SI()) for _ in range(H)]
    
    DH = [-1, -1, -1, 0, 0, 1, 1, 1, 0]
    DW = [-1, 0, 1, -1, 1, -1, 0, 1, 0]
    
    T = [["#"]*W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            for dh, dw in zip(DH, DW):
                nh, nw = h+dh, w+dw
                if 0 <= nh < H and 0 <= nw < W:
                    if S[nh][nw] == ".":
                        T[h][w] = "."

    U = [["."] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            for dh, dw in zip(DH, DW):
                nh, nw = h + dh, w + dw
                if 0 <= nh < H and 0 <= nw < W:
                    if T[nh][nw] == "#":
                        U[h][w] = "#"

    # print(*T, sep="\n")
    # print(*U, sep="\n")

    if S == U:
        print("possible")
        for row in T:
            print("".join(row))
    else:
        print("impossible")


if __name__ == "__main__":
    main()
