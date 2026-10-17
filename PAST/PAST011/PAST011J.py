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


def main():
    S = list(map(int, input().split("-")))
    T = list(map(int, input().split("-")))
    M = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    UM = M[:]
    UM[2] += 1
    CM = list(accumulate(M))
    CUM = list(accumulate(UM))

    def is_uruu(y):
        return y % 400 == 0 or (y % 4 == 0 and y % 100)

    def calc(X, is_S):
        xy, xm, xd = X
        days = 0
        for y in range(2022, xy):
            if is_uruu(y):
                days += 366
            else:
                days += 365

        days += CUM[xm-1] if is_uruu(xy) else CM[xm-1]
        days += xd

        if is_S:
            days -= 1

        # print(days)
        return days // 7 * 2 + min((days+7)%7, 2)

    # print(calc(S, 1))
    # print(calc(T, 0))
    print(calc(T, 0) - calc(S, 1))


if __name__ == "__main__":
    main()
