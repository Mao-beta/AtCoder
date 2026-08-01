import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    T = NI()
    for _ in range(T):
        px, py, qx, qy, rx, ry, sx, sy = NMI()
        ax, ay = -(qy-py), qx-px
        bx, by = -(sy-ry), sx-rx
        mx, my = px+qx, py+qy
        nx, ny = sx+rx, sy+ry
        gx, gy = nx-mx, ny-my
        if ax * by != ay * bx:
            print("Yes")
        elif ax * gy == ay * gx:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
