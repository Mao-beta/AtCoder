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


class X:
    def __init__(self, a, b, i):
        self.a = a
        self.b = b
        self.i = i

    def __lt__(self, other):
        if self.a * (other.a + other.b) == other.a * (self.a + self.b):
            return self.i < other.i
        else:
            return self.a * (other.a + other.b) > other.a * (self.a + self.b)


def main():
    N = NI()
    AB = EI(N)
    XX = [X(a, b, i) for i, (a, b) in enumerate(AB, start=1)]
    XX.sort()
    ans = [x.i for x in XX]
    print(*ans)


if __name__ == "__main__":
    main()
