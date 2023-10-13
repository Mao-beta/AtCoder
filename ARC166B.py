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


def main():
    N, a, b, c = NMI()
    P = NLI()
    lcm_ab = math.lcm(a, b)
    lcm_bc = math.lcm(b, c)
    lcm_ca = math.lcm(a, c)
    lcm_abc = math.lcm(a, b, c)

    def to_x(p, x):
        # pをxの倍数にするための最小回数
        t = (p + x-1) // x * x
        return t - p


    def get_triple(To_X):
        if len(To_X) < 3:
            return sorted([[x, i] for i, x in enumerate(To_X)])

        hq = []
        for i in range(3):
            heappush(hq, [-To_X[i], i])

        for i in range(3, len(To_X)):
            heappush(hq, [-To_X[i], i])
            heappop(hq)

        res = [[-x, i] for x, i in hq]
        return sorted(res)


    # To_A = sorted([[to_x(p, a), i] for i, p in enumerate(P)])[:3]
    # To_B = sorted([[to_x(p, b), i] for i, p in enumerate(P)])[:3]
    # To_C = sorted([[to_x(p, c), i] for i, p in enumerate(P)])[:3]
    # To_AB = sorted([[to_x(p, lcm_ab), i] for i, p in enumerate(P)])[:3]
    # To_BC = sorted([[to_x(p, lcm_bc), i] for i, p in enumerate(P)])[:3]
    # To_CA = sorted([[to_x(p, lcm_ca), i] for i, p in enumerate(P)])[:3]
    # To_ABC = sorted([[to_x(p, lcm_abc), i] for i, p in enumerate(P)])[:3]

    To_A = get_triple([to_x(p, a) for p in P])
    To_B = get_triple([to_x(p, b) for p in P])
    To_C = get_triple([to_x(p, c) for p in P])
    To_AB = get_triple([to_x(p, lcm_ab) for p in P])
    To_BC = get_triple([to_x(p, lcm_bc) for p in P])
    To_CA = get_triple([to_x(p, lcm_ca) for p in P])
    To_ABC = get_triple([to_x(p, lcm_abc) for p in P])

    ans = To_ABC[0][0]

    for p in product(To_AB, To_C):
        if p[0][1] == p[1][1]:
            continue
        ans = min(ans, p[0][0] + p[1][0])

    for p in product(To_BC, To_A):
        if p[0][1] == p[1][1]:
            continue
        ans = min(ans, p[0][0] + p[1][0])

    for p in product(To_CA, To_B):
        if p[0][1] == p[1][1]:
            continue
        ans = min(ans, p[0][0] + p[1][0])

    for p in product(To_A, To_B, To_C):
        if p[0][1] == p[1][1] or p[0][1] == p[2][1] or p[1][1] == p[2][1]:
            continue
        ans = min(ans, p[0][0] + p[1][0] + p[2][0])

    print(ans)


if __name__ == "__main__":
    main()
