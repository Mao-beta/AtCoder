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
    T = NI()
    for _ in range(T):
        ax, ay, bx, by, cx, cy = NMI()
        x = (ax*bx - ay*by) * cy - (ax*by + ay*bx) * cx
        y = (ax*bx - ay*by) * cx + (ax*by + ay*bx) * cy
        if x == 0 and y >= 0:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
