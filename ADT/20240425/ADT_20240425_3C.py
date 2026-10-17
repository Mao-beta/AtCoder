import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    DH = [1, -1, 0, 0, 1, -1, 1, -1]
    DW = [0, 0, 1, -1, 1, 1, -1, -1]

    def check(sh, sw, dh, dw):
        for i, s in enumerate("snuke"):
            h, w = sh+dh*i, sw+dw*i
            if h < 0 or h >= H or w < 0 or w >= W:
                return False
            if S[h][w] != s:
                return False
        return True

    for h in range(H):
        for w in range(W):
            for dh, dw in zip(DH, DW):
                if check(h, w, dh, dw):
                    for i in range(5):
                        print(h+dh*i+1, w+dw*i+1)
                    return



if __name__ == "__main__":
    main()
