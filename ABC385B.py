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
    H, W, X, Y = NMI()
    X -= 1
    Y -= 1
    S = [SI() for _ in range(H)]
    T = SI()
    ss = "UDLR"
    DH = [-1, 1, 0, 0]
    DW = [0, 0, -1, 1]
    seen = set()
    for t in T:
        # print(t)
        d = ss.index(t)
        X += DH[d]
        Y += DW[d]
        if not(0 <= X < H or 0 <= Y < W) or S[X][Y] == "#":
            X -= DH[d]
            Y -= DW[d]
            continue
        if S[X][Y] == "@":
            seen.add(X*W+Y)
    print(X+1, Y+1, len(seen))


if __name__ == "__main__":
    main()
