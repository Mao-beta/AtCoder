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
    X, Y, Z = NMI()
    P = [[X, 0], [Y, 1], [Z, 2]]
    P.sort()
    res = []
    x, y, z = P[0][0], P[1][0], P[2][0]
    if x == y:
        res.append([0] * x)
        res.append([0] * z)
        res.append([0] * z)
    else:
        res.append([0] * x + [1] * y)
        res.append([0] * z)
        res.append([1] * y + [0] * z)
    ans = [[], [], []]
    ans[P[0][1]] = res[0]
    ans[P[1][1]] = res[1]
    ans[P[2][1]] = res[2]
    for row in ans:
        print(len(row), *row)


if __name__ == "__main__":
    main()
