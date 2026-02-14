import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
from fractions import Fraction

sys.set_int_max_str_digits(10**6)
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
    from functools import cmp_to_key

    area = lambda x, y, i: 0 if y < 0 else 2 if x < 0 else 1

    def arg_cmp(p, q):
        ap = area(*p)
        aq = area(*q)
        if ap == aq:
            px, py, pi = p
            qx, qy, qi = q
            z = px * qy - py * qx
            return 1 if z > 0 else -1 if z < 0 else 0
        else:
            return 1 if ap < aq else -1

    N, Q = NMI()
    XYI = [NLI()+[i] for i in range(N)]
    XYI.sort(key=cmp_to_key(arg_cmp))
    # print(XYI)

    AB = EI(Q)
    AB = [[x-1, y-1] for x, y in AB]

    rpos = [0] * N
    rpos[XYI[-1][2]] = N-1
    for i in range(N-1, 0, -1):
        if i > 0 and arg_cmp(XYI[i-1], XYI[i]) == 0:
            rpos[XYI[i-1][2]] = rpos[XYI[i][2]]
        else:
            rpos[XYI[i-1][2]] = i-1
    # print(rpos)

    lpos = [0] * N
    lpos[XYI[-1][2]] = N - 1
    for i in range(N-1):
        if i < N-1 and arg_cmp(XYI[i], XYI[i+1]) == 0:
            lpos[XYI[i+1][2]] = lpos[XYI[i][2]]
        else:
            lpos[XYI[i+1][2]] = i+1
    # print(lpos)

    for a, b in AB:
        if rpos[XYI[0][2]] == rpos[XYI[-1][2]]:
            print(N)
            continue

        if rpos[a] == rpos[b]:
            print(rpos[a] - lpos[a] + 1)
            continue

        if lpos[a] < rpos[b]:
            print(rpos[b]-lpos[a]+1)
        else:
            print(N-(lpos[a]-(rpos[b]+1)))


if __name__ == "__main__":
    main()
