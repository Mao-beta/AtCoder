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
    DH = [0, 0, 1, -1, 1, 1, -1, -1]
    DW = [1, -1, 0, 0, 1, -1, 1, -1]

    def check(h, w, d):
        dh, dw = DH[d], DW[d]
        for x in range(5):
            nh, nw = h+dh*x, w+dw*x
            s = "snuke"[x]
            if 0 <= nh < H and 0 <= nw < W:
                if s != S[nh][nw]:
                    return False
            else:
                return False
        for x in range(5):
            nh, nw = h+dh*x, w+dw*x
            print(nh+1, nw+1)
        exit()

    for h in range(H):
        for w in range(W):
            for d in range(8):
                check(h, w, d)


if __name__ == "__main__":
    main()
