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
    C = [SI() for _ in range(H)]

    DH = [1, 1, -1, -1]
    DW = [1, -1, 1, -1]

    N = min(H, W)
    ans = [0] * (N+1)


    def check(sh, sw):
        if C[sh][sw] == ".":
            return 0
        for dh, dw in zip(DH, DW):
            if C[sh + dh][sw + dw] == ".":
                return 0

        h, w = sh, sw
        while h < H and w < W and C[h][w] == "#":
            h += 1
            w += 1

        return h - sh - 1


    for sh in range(1, H-1):
        for sw in range(1, W-1):
            res = check(sh, sw)
            ans[res] += 1

    print(*ans[1:])


if __name__ == "__main__":
    main()
