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


def main():
    H, W, K = NMI()
    C = [SI() for _ in range(H)]

    white = H * W
    for hs in range(1<<H):
        hk = bin(hs).count("1")
        if hk > K:
            continue

        rem = K - hk

        ws = [0] * W
        for h in range(H):
            if (hs >> h) & 1:
                continue
            for w in range(W):
                if C[h][w] == ".":
                    ws[w] += 1
        ws.sort()
        tmp = sum(ws)
        for k in range(rem):
            tmp -= ws[-k-1]
        white = min(white, tmp)

    print(H*W - white)


if __name__ == "__main__":
    main()
