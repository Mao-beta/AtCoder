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


def print_err(*args):
    print(*args, file=sys.stderr)


def convex(Vs):
    """
    :param Vs(sorted by x): [[x1, y1], ... [xn, yn]]
    :return: upper, lower
    """

    def cross(x1, y1, x2, y2):
        return x1 * y2 - y1 * x2

    def is_ccw(x1, y1, x2, y2):
        return cross(x1, y1, x2, y2) > 0

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


def dist(px, py, qx, qy):
    return math.sqrt((px-qx)**2 + (py-qy)**2)


def main():
    N = NI()
    XY = EI(N)
    S = NLI()
    T = NLI()

    V = [S] + XY + [T]
    V.sort()
    upper, lower = convex(V)
    upper.pop()
    lower.pop()
    C = list(upper + lower)
    L = len(C)

    si = -1
    ti = -1
    for i in range(L):
        if S == C[i]:
            si = i
        if T == C[i]:
            ti = i

    if min(si, ti) == -1:
        print(dist(*S, *T))
    else:
        if si > ti:
            si, ti = ti, si

        res1 = 0
        for i in range(si, ti):
            res1 += dist(*C[i], *C[(i+1)%L])

        res2 = 0
        for i in range(ti, si+L):
            res2 += dist(*C[i%L], *C[(i+1)%L])

        print(min(res1, res2))


if __name__ == "__main__":
    main()
