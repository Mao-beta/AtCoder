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
    X, Y = NMI()
    ans = 10**20

    # X, Y
    k = Y - X
    if k >= 0:
        ans = min(ans, k)

    # X, -Y
    k = -Y - X + 1
    if k >= 0:
        ans = min(ans, k)

    # -X, Y
    k = Y + X + 1
    if k >= 0:
        ans = min(ans, k)

    # -X, -Y
    k = -Y + X + 2
    if k >= 0:
        ans = min(ans, k)

    print(ans)


if __name__ == "__main__":
    main()
