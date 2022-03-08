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


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def dist2(self, other):
        return (self.x - other.x)**2 + (self.y - other.y)**2

    def relation(self, other):
        d2 = self.dist2(other)

        if d2 > (self.r + other.r)**2:
            # 背反
            return 5
        elif d2 == (self.r + other.r)**2:
            # 外接
            return 4
        elif d2 == (self.r - other.r)**2:
            # 内接
            return 2
        elif d2 < (self.r - other.r)**2:
            # 包含
            return 1
        else:
            # 交差
            return 3


def main():
    C1 = Circle(*NMI())
    C2 = Circle(*NMI())
    print(C1.relation(C2))


if __name__ == "__main__":
    main()
