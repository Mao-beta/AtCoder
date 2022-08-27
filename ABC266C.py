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
    P = [NLI() for _ in range(4)]
    P.append(P[0])
    P.append(P[1])

    for i in range(4):
        px, py = P[i]
        qx, qy = P[i+1]
        rx, ry = P[i+2]
        ax, ay = qx - px, qy - py
        bx, by = rx - qx, ry - qy

        if ax * by - bx * ay < 0:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
