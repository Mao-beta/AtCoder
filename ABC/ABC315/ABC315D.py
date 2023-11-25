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
    H2C = [[0]*26 for _ in range(H)]
    W2C = [[0]*26 for _ in range(W)]
    for h in range(H):
        for w in range(W):
            s = ord(C[h][w]) - ord("a")
            H2C[h][s] += 1
            W2C[w][s] += 1

    rh = H
    rw = W

    DH = [0] * 26
    DW = [0] * 26
    nrh = rh
    nrw = rw

    while True:
        # print(rh, rw, DH, DW, H2C, W2C)
        for key, val in enumerate(DH):
            for C in W2C:
                C[key] -= val
            DH[key] -= val

        for key, val in enumerate(DW):
            for C in H2C:
                C[key] -= val
            DH[key] -= val

        if rw >= 2:
            for h, C in enumerate(H2C):
                for s in range(26):
                    if C[s] == rw:
                        DH[s] += 1
                        C[s] = 0
                        nrh -= 1

        if rh >= 2:
            for w, C in enumerate(W2C):
                for s in range(26):
                    if C[s] == rh:
                        DW[s] += 1
                        C[s] = 0
                        nrw -= 1

        if rh == nrh and rw == nrw:
            break
        rh, rw = nrh, nrw



    # print(DH, DW)
    # print(rh, rw)
    print(rh * rw)


if __name__ == "__main__":
    main()
