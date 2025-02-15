import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    X, Y = NMI()
    DX = [-2, -2, -1, -1, 1, 1, 2, 2]
    DY = [-1, 1, 2, -2, 2, -2, 1, -1]
    S = set()
    S.add((0, 0))
    for x, y in list(S):
        for dx, dy in zip(DX, DY):
            S.add((x + dx, y + dy))
    for x, y in list(S):
        for dx, dy in zip(DX, DY):
            S.add((x + dx, y + dy))
    for x, y in list(S):
        for dx, dy in zip(DX, DY):
            S.add((x + dx, y + dy))
    if (X, Y) in S:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
