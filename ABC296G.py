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


# cross product: (b - a)×(c - a)
def cross3(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

# O(N)
def inside_convex_polygon0(p0, qs):
    L = len(qs)
    D = [cross3(qs[i-1], p0, qs[i]) for i in range(L)]
    return all(e >= 0 for e in D) or all(e <= 0 for e in D)

# O(log N)
def inside_convex_polygon(p0, qs):
    L = len(qs)

    def on_segment(P, A, B):
        if ((A[0] <= P[0] and P[0] <= B[0]) or (B[0] <= P[0] and P[0] <= A[0])):
            if ((A[1] <= P[1] and P[1] <= B[1]) or (B[1] <= P[1] and P[1] <= A[1])):
                if ((P[1] * (A[0] - B[0])) + (A[1] * (B[0] - P[0])) + (B[1] * (P[0] - A[0])) == 0):
                    return True
        return False

    if on_segment(p0, qs[0], qs[1]):
        return "ON"
    if on_segment(p0, qs[0], qs[-1]):
        return "ON"

    left = 1; right = L
    q0 = qs[0]
    while left+1 < right:
        mid = (left + right) >> 1
        if cross3(q0, p0, qs[mid]) <= 0:
            left = mid
        else:
            right = mid
    if left == L-1:
        left -= 1
    qi = qs[left]; qj = qs[left+1]
    v0 = cross3(q0, qi, qj)
    v1 = cross3(q0, p0, qj)
    v2 = cross3(q0, qi, p0)
    if v0 < 0:
        v1 = -v1; v2 = -v2

    if 0 <= v1 and 0 <= v2 and v1 + v2 == v0:
        return "ON"
    elif 0 <= v1 and 0 <= v2 and v1 + v2 <= v0:
        return "IN"
    else:
        return "OUT"


def main():
    N = NI()
    qs = EI(N)
    Q = NI()
    AB = EI(Q)
    for a, b in AB:
        res = inside_convex_polygon((a, b), qs)
        print(res)


if __name__ == "__main__":
    main()
