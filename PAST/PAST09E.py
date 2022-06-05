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


def state(s):
    if s in "12345":
        res = 0
    else:
        res = 1
    return res


def main():
    N = SI()
    prev = None
    ans = 0
    for s in N:
        if prev is None:
            ans += 500
        elif s == prev:
            ans += 301
        elif state(prev) == state(s):
            ans += 210
        else:
            ans += 100

        prev = s

    print(ans)


if __name__ == "__main__":
    main()
