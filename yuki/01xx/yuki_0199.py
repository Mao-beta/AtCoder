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


def convex(Vs):
    """
    :param Vs(sorted by x): [[x1, y1], ... [xn, yn]]
    :return: upper, lower
    """

    def cross(x1, y1, x2, y2):
        return x1 * y2 - y1 * x2

    def is_ccw(x1, y1, x2, y2):
        return cross(x1, y1, x2, y2) >= 0

    N = len(Vs)

    upper = deque()
    upper.append(Vs[0])
    upper.append(Vs[1])

    for i in range(2, N):
        V3 = Vs[i]
        x3, y3 = V3

        while len(upper) >= 2:
            V2 = upper.pop()
            V1 = upper.pop()
            x2, y2 = V2
            x1, y1 = V1

            upper.append(V1)

            if not is_ccw(x2-x1, y2-y1, x3-x2, y3-y2):
                upper.append(V2)
                upper.append(V3)
                break

        if len(upper) < 2:
            upper.append(V3)


    lower = deque()
    lower.append(Vs[-1])
    lower.append(Vs[-2])

    for i in range(N-3, -1, -1):
        V3 = Vs[i]
        x3, y3 = V3

        while len(lower) >= 2:
            V2 = lower.pop()
            V1 = lower.pop()
            x2, y2 = V2
            x1, y1 = V1

            lower.append(V1)

            if not is_ccw(x2-x1, y2-y1, x3-x2, y3-y2):
                lower.append(V2)
                lower.append(V3)
                break

        if len(lower) < 2:
            lower.append(V3)

    return upper, lower


def convex_perimeter(upper: deque, lower: deque):
    res = 0
    x, y = upper.popleft()
    while upper:
        xx, yy = upper.popleft()
        res += math.sqrt((x - xx) ** 2 + (y - yy) ** 2)
        x, y = xx, yy

    x, y = lower.popleft()
    while lower:
        xx, yy = lower.popleft()
        res += math.sqrt((x - xx) ** 2 + (y - yy) ** 2)
        x, y = xx, yy

    return res


def main():
    XY = EI(5)
    XY.sort()
    upper, lower = convex(XY)
    if len(upper) + len(lower) == 7:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
