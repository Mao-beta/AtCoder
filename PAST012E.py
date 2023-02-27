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
    R, N, M, L = NMI()
    S = NLI()

    r = 0
    n = 0
    m = 0
    for s in S:
        n += s
        m += 1
        if n == N or m == M:
            n = 0
            r += 1
            m = 0
        elif n > N:
            print("No")
            exit()

    if r > R or m > 0:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
