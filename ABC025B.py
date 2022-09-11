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
    N, A, B = NMI()
    now = 0
    for i in range(N):
        s, d = SMI()
        d = int(d)
        if d < A:
            d = A
        elif d > B:
            d = B

        if s == "East":
            d = int(d)
        else:
            d = int(d) * (-1)

        now += d

    if now > 0:
        print("East", now)
    elif now < 0:
        print("West", abs(now))
    else:
        print(0)


if __name__ == "__main__":
    main()
