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
    N = NI()
    T = NLI()
    a = 0
    for t in T:
        if a == 0 and t == 0:
            a = 1
            continue

        tmp = a
        an = 0
        while tmp % 2 == 0 and tmp > 0:
            an += 1
            tmp //= 2

        if an > t:
            a += 1 << t
        else:
            r = a % (1 << (t+1))
            if r < (1 << t):
                a = a - r + (1 << t)
            else:
                a = (((a >> (t+1)) + 1) << (t+1)) + (1 << t)

        # print(bin(a)[2:].zfill(10))

    print(a)


if __name__ == "__main__":
    main()
