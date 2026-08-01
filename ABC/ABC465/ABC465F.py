import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from itertools import accumulate, combinations, permutations, product

MOD = 10 ** 9 + 7
MOD99 = 998244353

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def ff(a, b, c, d, e, f):
    res = a * 11 ** 5 + b * 11 ** 4 + c * 11 ** 3 + d * 11 ** 2 + e * 11 + f
    return res


def main():
    N = NI()
    SV = [SLI() for _ in range(N)]
    Q = NI()
    XY = [SLI() for _ in range(Q)]
    # imos = [[[[[[0]*11 for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)]
    imos = [0] * 11 ** 6
    for s, v in SV:
        x = ff(int(s[0]) + 1, int(s[1]) + 1, int(s[2]) + 1, int(s[3]) + 1, int(s[4]) + 1, int(s[5]) + 1)
        imos[x] += int(v)
        # imos[int(s[0])+1][int(s[1])+1][int(s[2])+1][int(s[3])+1][int(s[4])+1][int(s[5])+1] += int(v)
    for a in range(11):
        for b in range(11):
            for c in range(11):
                for d in range(11):
                    for e in range(11):
                        for f in range(10):
                            imos[ff(a, b, c, d, e, f + 1)] += imos[ff(a, b, c, d, e, f)]
    for a in range(11):
        for b in range(11):
            for c in range(11):
                for d in range(11):
                    for e in range(10):
                        for f in range(11):
                            imos[ff(a, b, c, d, e + 1, f)] += imos[ff(a, b, c, d, e, f)]
    for a in range(11):
        for b in range(11):
            for c in range(11):
                for d in range(10):
                    for e in range(11):
                        for f in range(11):
                            imos[ff(a, b, c, d + 1, e, f)] += imos[ff(a, b, c, d, e, f)]
    for a in range(11):
        for b in range(11):
            for c in range(10):
                for d in range(11):
                    for e in range(11):
                        for f in range(11):
                            imos[ff(a, b, c + 1, d, e, f)] += imos[ff(a, b, c, d, e, f)]
    for a in range(11):
        for b in range(10):
            for c in range(11):
                for d in range(11):
                    for e in range(11):
                        for f in range(11):
                            imos[ff(a, b + 1, c, d, e, f)] += imos[ff(a, b, c, d, e, f)]
    for a in range(10):
        for b in range(11):
            for c in range(11):
                for d in range(11):
                    for e in range(11):
                        for f in range(11):
                            imos[ff(a + 1, b, c, d, e, f)] += imos[ff(a, b, c, d, e, f)]

    for x, y in XY:
        ok = True
        for i in range(6):
            if int(x[i]) > int(y[i]):
                ok = False
        if not ok:
            print(0)
            continue
        r0, r1, r2, r3, r4, r5 = int(y[0]) + 1, int(y[1]) + 1, int(y[2]) + 1, int(y[3]) + 1, int(y[4]) + 1, int(
            y[5]) + 1
        l0, l1, l2, l3, l4, l5 = int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5])
        ans = 0
        for b, P in enumerate(product([l0, r0], [l1, r1], [l2, r2], [l3, r3], [l4, r4], [l5, r5])):
            bc = sum((b >> i) & 1 for i in range(6))
            ans += imos[ff(P[0], P[1], P[2], P[3], P[4], P[5])] * (-1) ** bc
            # ans += imos[P[0]][P[1]][P[2]][P[3]][P[4]][P[5]] * (-1) ** bc
        print(ans)


if __name__ == "__main__":
    main()
