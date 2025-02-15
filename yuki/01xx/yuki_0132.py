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


def cross3(X, Y):
    """3次元ベクトルXとYの外積"""
    return [X[(i+1)%3]*Y[(i+2)%3]-X[(i+2)%3]*Y[(i+1)%3] for i in range(3)]


def dist_P_from_plane_of_3points(P, Qs):
    """
    3次元空間において、点Pと、3点Qsで張られる平面との距離
    """
    Q0 = [p - x for p, x in zip(P, Qs[0])]
    Q1 = [p - x for p, x in zip(P, Qs[1])]
    Q2 = [p - x for p, x in zip(P, Qs[2])]
    Q01 = [Q1[i] - Q0[i] for i in range(3)]
    Q02 = [Q2[i] - Q0[i] for i in range(3)]
    R = cross3(Q01, Q02)
    a, b, c = R
    x, y, z = Q0
    d = a*x + b*y + c*z
    return abs(d / math.sqrt(a**2+b**2+c**2))


def main():
    N = NI()
    # P = [int(s.replace(".", "")) for s in SLI()]
    P = list(map(float, SMI()))
    XYZ = []
    for _ in range(N):
        # xyz = [int(s.replace(".", "")) for s in SLI()]
        xyz = list(map(float, SMI()))
        XYZ.append(xyz)

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                ans += dist_P_from_plane_of_3points(P, [XYZ[i], XYZ[j], XYZ[k]])

    # print(ans / 10**6)
    print(ans)


if __name__ == "__main__":
    main()
