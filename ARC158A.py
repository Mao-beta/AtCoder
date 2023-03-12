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


def solve(a, b, c):
    M = min(a, b, c)
    a, b, c = sorted([a, b, c])
    a -= M
    b -= M
    c -= M
    if (a + b + c) % 6 or b % 2 or c % 2:
        return -1

    if c > 2 * b:
        ans = b // 2 + (c - 2*b) // 3
    else:
        ans = (2*b - c) // 3 + (c-b) // 2

    return ans


def main():
    T = NI()
    for _ in range(T):
        a, b, c = NMI()
        ans = solve(a, b, c)
        print(ans)


if __name__ == "__main__":
    main()
