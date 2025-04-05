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
    hl, hr, wl, wr = H, 0, W, 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                hl, hr, wl, wr = min(h, hl), max(h, hr), min(w, wl), max(w, wr)
    for h in range(H):
        for w in range(W):
            if hl <= h <= hr and wl <= w <= wr:
                if S[h][w] == ".":
                    print("No")
                    return
            else:
                if S[h][w] == "#":
                    print("No")
                    return
    print("Yes")


if __name__ == "__main__":
    main()
