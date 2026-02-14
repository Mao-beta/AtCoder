import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
from fractions import Fraction

sys.set_int_max_str_digits(10 ** 6)
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
        ax, ay, az = NMI()
        bx, by, bz = NMI()
        cx, cy, cz = NMI()
        lx, ly, lz = NMI()
        px = Fraction(lx) - Fraction((lx - ax) * lz, lz - az)
        py = Fraction(ly) - Fraction((ly - ay) * lz, lz - az)
        qx = Fraction(lx) - Fraction((lx - bx) * lz, lz - bz)
        qy = Fraction(ly) - Fraction((ly - by) * lz, lz - bz)
        rx = Fraction(lx) - Fraction((lx - cx) * lz, lz - cz)
        ry = Fraction(ly) - Fraction((ly - cy) * lz, lz - cz)
        # print(px, py, qx, qy, rx, ry)
        dx = qx - px
        dy = qy - py
        ex = rx - px
        ey = ry - py
        S = abs(dx * ey - dy * ex) / 2
        print(S.numerator % MOD99 * pow(S.denominator % MOD99, -1, MOD99) % MOD99)


if __name__ == "__main__":
    main()
