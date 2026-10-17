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
    N = NI()
    S = SI()
    P = {(0, 0)}
    x, y = 0, 0
    DXY = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}
    for s in S:
        dx, dy = DXY[s]
        nx, ny = x+dx, y+dy
        if (nx, ny) in P:
            print("Yes")
            return
        P.add((nx, ny))
        x, y = nx, ny
    print("No")


if __name__ == "__main__":
    main()
