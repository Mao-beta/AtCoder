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
    K = NI()
    x1, y1 = NMI()
    x2, y2 = NMI()
    x = abs(x2-x1)
    y = abs(y2-y1)
    if x < y:
        x, y = y, x
    ans = (x+y+2*K-1) // (2*K) + (x-y+2*K-1) // (2*K)
    print(ans)


if __name__ == "__main__":
    main()
