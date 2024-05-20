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
    T = SI()
    DX = [1, 0, -1, 0]
    DY = [0, -1, 0, 1]
    d = 0
    X, Y = 0, 0
    for s in T:
        if s == "S":
            dx, dy = DX[d], DY[d]
            X += dx
            Y += dy
        else:
            d = (d+1) % 4
    print(X, Y)


if __name__ == "__main__":
    main()
