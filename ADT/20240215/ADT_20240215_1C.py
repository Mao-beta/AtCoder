import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    snuke = "snuke"
    DH = [1, -1, 0, 0, 1, 1, -1, -1]
    DW = [0, 0, 1, -1, 1, -1, 1, -1]

    def check(h, w, dh, dw):
        res = []
        for i in range(5):
            nh, nw = h+dh*i, w+dw*i
            if nh < 0 or nh >= H or nw < 0 or nw >= W:
                return []
            if S[nh][nw] != snuke[i]:
                return []
            res.append([nh+1, nw+1])
        return res

    for h in range(H):
        for w in range(W):
            for dh, dw in zip(DH, DW):
                res = check(h, w, dh, dw)
                if res:
                    for h, w in res:
                        print(h, w)




if __name__ == "__main__":
    main()
