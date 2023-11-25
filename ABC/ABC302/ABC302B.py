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
    S = [SI() for _ in range(H)]

    DH = [0, 0, 1, -1, 1, 1, -1, -1]
    DW = [1, -1, 0, 0, 1, -1, 1, -1]

    def check(h, w, dh, dw):
        if 0 <= h + dh * 4 < H and 0 <= w + dw * 4 < W:
            for i in range(5):
                if S[h+dh*i][w+dw*i] != "snuke"[i]:
                    return False
            return True
        else:
            return False

    for h in range(H):
        for w in range(W):
            if S[h][w] != "s":
                continue
            for dh, dw in zip(DH, DW):
                if check(h, w, dh, dw):
                    for i in range(5):
                        print(h + dh * i + 1, w + dw * i + 1)



if __name__ == "__main__":
    main()
