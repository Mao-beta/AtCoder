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
    l, r, u, d = W, 0, H, 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                l = min(l, w)
                u = min(u, h)
                r = max(r, w)
                d = max(d, h)

    for h in range(u, d+1):
        for w in range(l, r+1):
            if S[h][w] == ".":
                print(h+1, w+1)
                return


if __name__ == "__main__":
    main()
