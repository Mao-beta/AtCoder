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
    N, x, y = NMI()
    A = NLI()

    yoko = A[::2]
    tate = A[1::2]

    # -10000 ～ 10000
    M = 20001

    if N == 2:
        if x != A[0]:
            print("No")

        dpx = [[0]*(M+1) for _ in range(len(yoko)+1)]
        dpx[-1][x] = 1

    else:
        yoko = yoko[1:]
        dpx = [[0]*(M+1) for _ in range(len(yoko)+1)]
        dpx[0][A[0]] = 1
        for i, a in enumerate(yoko):
            for j in range(-10000, 10001):
                if dpx[i][j] == 0:
                    continue

                dpx[i+1][j+a] |= dpx[i][j]
                dpx[i+1][j-a] |= dpx[i][j]

    dpy = [[0]*(M+1) for _ in range(len(tate)+1)]
    dpy[0][0] = 1
    for i, a in enumerate(tate):
        for j in range(-10000, 10001):
            if dpy[i][j] == 0:
                continue

            dpy[i+1][j+a] |= dpy[i][j]
            dpy[i+1][j-a] |= dpy[i][j]

    if dpx[-1][x] and dpy[-1][y]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
