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
    H, W, D = NMI()
    if H > W:
        H, W = W, H

    def circle(d, rad):
        return rad/2 * d * d

    def p(area):
        return area / (H*W)

    if D < H/2:
        print(p(circle(D, math.pi*2)))

    elif D < W/2:
        a = math.acos(H / 2 / D)
        theta = math.pi - a * 2
        area = circle(D, theta*2) + H/2 * H/2 * math.tan(a) * 2
        print(p(area))

    elif D**2 * 4 < H**2 + W**2:
        ah = math.acos(H / 2 / D)
        aw = math.acos(W / 2 / D)
        area = circle(D, math.pi*2 - 4*ah - 4*aw)
        area += H/2 * H/2 * math.tan(ah) * 2
        area += W/2 * W/2 * math.tan(aw) * 2
        print(p(area))

    else:
        print(1)


if __name__ == "__main__":
    main()
