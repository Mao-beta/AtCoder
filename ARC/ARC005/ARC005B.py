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
    w, h, W = SMI()
    w, h = int(w)-1+8, int(h)-1+8
    C = [list(SI()) for _ in range(9)]
    
    A = [c[1:][::-1] + c[:] + c[:-1][::-1] for c in C]
    B = A[1:][::-1] + A[:] + A[:-1][::-1]

    ans = []
    S = ["R", "L", "U", "D", "RU", "RD", "LU", "LD"]
    DW = [1, -1, 0, 0, 1, 1, -1, -1]
    DH = [0, 0, -1, 1, -1, 1, -1, 1]
    dw, dh = DW[S.index(W)], DH[S.index(W)]
    for i in range(4):
        ans.append(B[h+dh*i][w+dw*i])
    print("".join(ans))


if __name__ == "__main__":
    main()
