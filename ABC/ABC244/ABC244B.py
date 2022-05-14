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
    S = SI()
    DX = [1, 0, -1, 0]
    DY = [0, -1, 0, 1]
    idx = 0
    x, y = 0, 0
    for s in S:
        if s == "S":
            dx = DX[idx]
            dy = DY[idx]
            x += dx
            y += dy
        else:
            idx = (idx + 1) % 4
    print(x, y)


if __name__ == "__main__":
    main()
