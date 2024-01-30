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
    N = NI()
    XY = EI(N)
    ans = 0
    for P in combinations(XY, 3):
        p, q, r = P
        x1 = q[0] - p[0]
        y1 = q[1] - p[1]
        x2 = r[0] - p[0]
        y2 = r[1] - p[1]
        s2 = abs(x1 * y2 - y1 * x2)
        if s2 > 0 and s2 % 2 == 0:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
