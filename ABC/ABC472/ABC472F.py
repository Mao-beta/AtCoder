import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    # https://ja.wikipedia.org/wiki/%E5%B9%BE%E4%BD%95%E4%B8%AD%E5%BF%83
    N, Q = NMI()
    XY = EI(N)
    UV = EI(Q)
    UV = [[x-1, y-1 if x < y else y-1+N] for x, y in UV]
    Bx = [0] * N
    By = [0] * N
    A = [0] * N
    for i in range(N):
        xi, yi = XY[i]
        xj, yj = XY[(i+1)%N]
        Bx[i] = (xi+xj) * (xi*yj - xj*yi)
        By[i] = (yi+yj) * (xi*yj - xj*yi)
        A[i] = xi*yj - xj*yi

    Bx *= 2
    By *= 2
    A *= 2
    Cx = list(accumulate([0]+Bx))
    Cy = list(accumulate([0]+By))
    CA = list(accumulate([0]+A))

    for u, v in UV:
        xu, yu = XY[u]
        xv, yv = XY[v%N]
        cx = Cx[v] - Cx[u] + (xu+xv) * (xv*yu - xu*yv)
        cy = Cy[v] - Cy[u] + (yu+yv) * (xv*yu - xu*yv)
        a = CA[v] - CA[u] + (xv*yu - xu*yv)
        print(cx / a / 3, cy / a / 3)


if __name__ == "__main__":
    main()
