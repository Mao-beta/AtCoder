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
    N = NI()

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f"{self.x} {self.y}"

    cos = math.cos(math.pi/3)
    sin = math.sin(math.pi/3)

    def make(P1: Point, P2: Point):
        sx = (P1.x * 2 + P2.x * 1) / 3
        tx = (P1.x * 1 + P2.x * 2) / 3
        sy = (P1.y * 2 + P2.y * 1) / 3
        ty = (P1.y * 1 + P2.y * 2) / 3
        gx = tx - sx
        gy = ty - sy
        ux = sx + cos * gx - sin * gy
        uy = sy + sin * gx + cos * gy
        return [P1, Point(sx, sy), Point(ux, uy), Point(tx, ty), P2]

    def coch(Ps):
        n = len(Ps)
        res = [Ps[0]]
        for i in range(n-1):
            P1 = Ps[i]
            P2 = Ps[i+1]
            res += make(P1, P2)[1:]
        return res

    Ps = [Point(0, 0), Point(100, 0)]
    for i in range(N):
        Ps = coch(Ps)
    print(*Ps, sep="\n")


if __name__ == "__main__":
    main()
