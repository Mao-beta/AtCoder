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
    h, w = NMI()
    h -= 1
    w -= 1
    C = [SI() for _ in range(H)]
    X = SI()
    D = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
    for s in X:
        dh, dw = D[s]
        nh, nw = h+dh, w+dw
        if 0 <= nh < H and 0 <= nw < W and C[nh][nw] == ".":
            h, w = nh, nw
    print(h+1, w+1)


if __name__ == "__main__":
    main()
