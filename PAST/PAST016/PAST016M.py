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


def cross(x1, y1, x2, y2):
    return x1 * y2 - y1 * x2

def dot(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2


def _intersect(a1, b1, c1, d1, a2, b2, c2, d2):
    # 線分の交差判定
    v1x, v1y = c1-a1, d1-b1
    a2a1, b2b1 = a2-a1, b2-b1
    c2a1, d2b1 = c2-a1, d2-b1
    C11 = cross(v1x, v1y, a2a1, b2b1)
    C12 = cross(v1x, v1y, c2a1, d2b1)

    v2x, v2y = c2-a2, d2-b2
    a1a2, b1b2 = a1-a2, b1-b2
    c1a2, d1b2 = c1-a2, d1-b2
    C21 = cross(v2x, v2y, a1a2, b1b2)
    C22 = cross(v2x, v2y, c1a2, d1b2)

    if C11 * C12 < 0 and C21 * C22 < 0:
        print("Yes")
    elif C11 * C12 > 0 or C21 * C22 > 0:
        print("No")
    elif C11 * C12 == 0 and C21 * C22 < 0:
        print("Yes")
    elif C11 * C12 < 0 and C21 * C22 == 0:
        print("Yes")
    elif C11 * C12 == 0 and C21 * C22 > 0:
        print("No")
    elif C11 * C12 > 0 and C21 * C22 == 0:
        print("No")
    else:
        if dot(a2a1, b2b1, c2a1, d2b1) <= 0:
            print("Yes")
        elif dot(a2-c1, b2-d1, c2-c1, d2-d1) <= 0:
            print("Yes")
        elif dot(a1a2, b1b2, c1a2, d1b2) <= 0:
            print("Yes")
        elif dot(a1-c2, b1-d2, c1-c2, d1-d2) <= 0:
            print("Yes")
        else:
            print("No")


# 線分同士の交点判定
def dot3(O, A, B):
    ox, oy = O; ax, ay = A; bx, by = B
    return (ax - ox) * (bx - ox) + (ay - oy) * (by - oy)
def cross3(O, A, B):
    ox, oy = O; ax, ay = A; bx, by = B
    return (ax - ox) * (by - oy) - (bx - ox) * (ay - oy)
def dist2(A, B):
    ax, ay = A; bx, by = B
    return (ax - bx) ** 2 + (ay - by) ** 2
def is_intersection(P0, P1, Q0, Q1):
    C0 = cross3(P0, P1, Q0)
    C1 = cross3(P0, P1, Q1)
    D0 = cross3(Q0, Q1, P0)
    D1 = cross3(Q0, Q1, P1)
    if C0 == C1 == 0:
        E0 = dot3(P0, P1, Q0)
        E1 = dot3(P0, P1, Q1)
        if not E0 < E1:
            E0, E1 = E1, E0
        return E0 <= dist2(P0, P1) and 0 <= E1
    return C0 * C1 <= 0 and D0 * D1 <= 0


def main():
    a1, b1, c1, d1 = NMI()
    a2, b2, c2, d2 = NMI()
    if is_intersection((a1, b1), (c1, d1), (a2, b2), (c2, d2)):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
