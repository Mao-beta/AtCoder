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


def intersect(Plow, Phigh, Qlow, Qhigh):
    Rlow = Plow[:]
    Rhigh = Phigh[:]
    for i in range(3):
        Rlow[i] = max(Rlow[i], Qlow[i])
        Rhigh[i] = min(Rhigh[i], Qhigh[i])
        if Rlow[i] > Rhigh[i]:
            Rhigh[i] = Rlow[i]
    return Rlow, Rhigh


def union(Plow, Phigh, Qlow, Qhigh):
    Rlow = Plow[:]
    Rhigh = Phigh[:]
    for i in range(3):
        Rlow[i] = min(Rlow[i], Qlow[i])
        Rhigh[i] = max(Rhigh[i], Qhigh[i])
        if Rlow[i] > Rhigh[i]:
            Rhigh[i] = Rlow[i]
    return [list(range(Rlow[i]-7, Rhigh[i])) for i in range(3)]


def v(low, high):
    res = 1
    for l, h in zip(low, high):
        res *= abs(h-l)
    return res


def main():
    V = [0] + NLI()
    P1low = [0, 0, 0]
    P1high = [7, 7, 7]
    for P2low in product(range(8), repeat=3):
        P2low = list(P2low)
        P2high = [p+7 for p in P2low]
        U12 = union(P1low, P1high, P2low, P2high)
        for P3low in product(*U12):
            # print(P3low)
            P3low = list(P3low)
            P3high = [p + 7 for p in P3low]
            P12low, P12high = intersect(P1low, P1high, P2low, P2high)
            P123low, P123high = intersect(P12low, P12high, P3low, P3high)
            v123 = v(P123low, P123high)

            # if [*P2low, *P3low] == [0, 6, 0, 6, 0, 0]:
            #     print(v123)
            if v123 != V[3]:
                continue

            P13low, P13high = intersect(P1low, P1high, P3low, P3high)
            P23low, P23high = intersect(P2low, P2high, P3low, P3high)
            v12 = v(P12low, P12high)
            v13 = v(P13low, P13high)
            v23 = v(P23low, P23high)
            # if [*P2low, *P3low] == [0, 6, 0, 6, 0, 0]:
            #     print(v12, v23, v13)
            if v12 + v13 + v23 - V[3] * 3 != V[2]:
                continue
            # if [*P2low, *P3low] == [0, 6, 0, 6, 0, 0]:
            #     print(343 * 3 - V[2] * 2 - V[3],V[1])
            if 343 * 3 - V[2] * 2 - V[3] * 3 != V[1]:
                continue
            print("Yes")
            print(*P1low, *P2low, *P3low)
            return

    print("No")


if __name__ == "__main__":
    main()
