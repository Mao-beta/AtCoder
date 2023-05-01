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
    A, B = NMI()
    if A > B:
        A, B = B, A

    if 3*B*B >= 4*A*A:
        print(A * math.sqrt(3) * 2 / 3)
        exit()

    p = math.pi * 15 / 180
    s = math.sin(p)
    c = math.cos(p)
    ans = math.sqrt((A+B)**2 * s**2 + (B-A)**2 * c**2) / (2*s*c)
    print(ans)



if __name__ == "__main__":
    main()
