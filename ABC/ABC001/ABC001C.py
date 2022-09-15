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
    deg, dis = NMI()
    deg *= 10
    dis *= 10

    DEG = [(i*2+1) * 1125 for i in range(16)]
    DEGS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N"]

    deg_i = bisect.bisect_left(DEG, deg)

    DIS = [25, 155, 335, 545, 795, 1075, 1385, 1715, 2075, 2445, 2845, 3265]
    DIS = [d*6 for d in DIS]
    dis_i = bisect.bisect_right(DIS, dis)
    if dis_i == 0:
        print("C", end=" ")
    else:
        print(DEGS[deg_i], end=" ")
    print(dis_i)



if __name__ == "__main__":
    main()
