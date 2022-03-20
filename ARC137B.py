import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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
    A = NLI()
    A = [1 if a == 1 else -1 for a in A]
    C = list(accumulate(A))

    p = 0
    m = 0
    bottom = 0
    top = 0
    for c in C:
        if c > bottom:
            p = max(p, c - bottom)
        else:
            bottom = c

        if c < top:
            m = max(m, top - c)
        else:
            top = c

    print(p+m+1)


if __name__ == "__main__":
    main()
