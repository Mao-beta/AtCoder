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
    Aw, Ab = NMI()
    Bw, Bb = NMI()
    C, D = NMI()
    if Ab >= C:
        Ab -= C
        Bb += C
    else:
        Bb += Ab
        Aw -= C-Ab
        Bw += C-Ab
        Ab = 0

    if Bw >= D:
        print(Aw + D)
    else:
        print(Aw + Bw)


if __name__ == "__main__":
    main()
