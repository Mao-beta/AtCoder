import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    N, M, A, B = NMI()
    C = [NI() for _ in range(M)]
    now = N
    for i, c in enumerate(C, start=1):
        if now <= A:
            now += B
        now -= c
        if now < 0:
            print(i)
            return
    print("complete")


if __name__ == "__main__":
    main()
