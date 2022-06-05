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


def rotate90(P):
    """90度回転して左上に合わせる"""
    ch, cw = P[0]
    res = [[h - ch, w - cw] for h, w in P]
    res = [[w, -h] for h, w in res]
    return res


def main():
    H, W = NMI()
    S = [SI() for _ in range(H)]
    T = [SI() for _ in range(H)]

    TP = []
    for h in range(H):
        for w in range(W):
            if T[h][w] == "#":
                TP.append([h, w])

    for i in range(4):
        TP = rotate90(TP)

        for th in range(H):
            for tw in range(W):
                ok = True
                for h, w in TP:
                    h += th
                    w += tw
                    if h < 0 or h >= H or w < 0 or w >= W:
                        ok = False
                        break
                    if S[h][w] == "#":
                        ok = False
                        break
                if ok:
                    print("Yes")
                    # print(TP, th, tw)
                    exit()

    print("No")


if __name__ == "__main__":
    main()
