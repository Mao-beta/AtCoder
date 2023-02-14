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
    a, b = NMI()
    P = NLI()
    Q = NLI()
    ans = [["x", " ", "x", " ", "x", " ", "x"],
           [" ", "x", " ", "x", " ", "x"],
           [" ", " ", "x", " ", "x"],
           [" ", " ", " ", "x"]
           ]

    D = [[0, 6], [3, 3], [2, 2], [2, 4], [1, 1], [1, 3], [1, 5], [0, 0], [0, 2], [0, 4]]
    for p in P:
        x, y = D[p]
        ans[x][y] = "."
    for q in Q:
        x, y = D[q]
        ans[x][y] = "o"

    for row in ans:
        print("".join(row))


if __name__ == "__main__":
    main()
