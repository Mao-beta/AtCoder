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
    A = EI(H)
    B = EI(H)
    for h in range(H):
        for w in range(W):
            if B[h][w] == -1:
                continue
            B[h][w] ^= A[h][w]

    rowX = [[-1]*H for _ in range(H)]
    for h1 in range(H):
        for h2 in range(h1+1, H):
            for w in range(W):
                if B[h1][w] == -1 or B[h2][w] == -1:
                    continue
                x = B[h1][w] ^ B[h2][w]
                r = rowX[h1][h2]
                if r == -1:
                    rowX[h1][h2] = x
                elif r == x:
                    continue
                else:
                    print("No")
                    return

    colX = [[-1] * W for _ in range(W)]
    for w1 in range(W):
        for w2 in range(w1+1, W):
            for h in range(H):
                if B[h][w1] == -1 or B[h][w2] == -1:
                    continue
                x = B[h][w1] ^ B[h][w2]
                r = colX[w1][w2]
                if r == -1:
                    colX[w1][w2] = x
                elif r == x:
                    continue
                else:
                    print("No")
                    return

    print("Yes")



if __name__ == "__main__":
    main()
