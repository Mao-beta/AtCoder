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
    TA = "Takahashi"
    AO = "Aoki"

    N, M = NMI()
    XY = [NLI() for _ in range(M)]

    if M == 0:
        if N % 2:
            print(TA)
        else:
            print(AO)
        exit()

    l = 1
    yl = 0
    g = 0
    for x, y in XY:
        if x == l:
            l = x+1
            yl = y
            continue

        if l == 1:
            # print(f"f{x-1}")
            g ^= x-1
            l = x+1
            yl = y

        else:
            if yl == y:
                # print(f"s{x-1 - l + 1}")
                g ^= 1
            else:
                # print(f"d{x-1 - l + 1}")
                pass
            l = x + 1
            yl = y

    if l <= N:
        # print(f"f{N-l+1}")
        g ^= N-l+1

    if g:
        print(TA)
    else:
        print(AO)


if __name__ == "__main__":
    main()
