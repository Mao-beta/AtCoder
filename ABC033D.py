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


EPS = 1e-9

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = math.atan2(y, x) * 180 / math.pi


def main():
    N = NI()
    XY = [NLI() for _ in range(N)]

    dull = 0
    rect = 0

    for i in range(N):
        cx, cy = XY[i]
        P = [Point(x-cx, y-cy) for x, y in XY if x != cx or y != cy]

        A = [p.angle for p in P]
        A += [a+360 for a in A] + [-1000, 1000]
        A.sort()

        for j in range(1, N):
            a = A[j]
            b = a + 90
            c = a + 180
            l = bisect.bisect_left(A, b-EPS)
            r = bisect.bisect_right(A, c+EPS)
            # print(A)
            # print(a, b, c, l, r)
            if abs(A[l] - b) < EPS:
                rect += 1
                dull += r - l - 1
            else:
                dull += r - l

            # print("a", rect, dull)

    total = N * (N-1) * (N-2) // 6
    print(total - rect - dull, rect, dull)


if __name__ == "__main__":
    main()
