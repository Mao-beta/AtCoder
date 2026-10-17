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
    N, K = NMI()
    xs, ys, xt, yt = NMI()
    PQRW = EI(N)

    def is_cross(p, q, r):
        s = (p * xs + q * ys - r > 0)
        t = (p * xt + q * yt - r > 0)
        return s ^ t

    C = []

    for p, q, r, w in PQRW:
        if is_cross(p, q, r):
            C.append(w)
        else:
            C.append(0)

    C.sort()
    print(sum(C[:K]))


if __name__ == "__main__":
    main()
