import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    x1, y1, r = NMI()
    x2, y2, x3, y3 = NMI()
    if x2 <= x1-r and x1+r <= x3 and y2 <= y1-r and y1+r <= y3:
        print("NO")
        print("YES")
    elif ((x2-x1)**2 + (y2-y1)**2 <= r**2 and (x2-x1)**2 + (y3-y1)**2 <= r**2 and
          (x3-x1)**2 + (y2-y1)**2 <= r**2 and (x3-x1)**2 + (y3-y1)**2 <= r**2):
        print("YES")
        print("NO")
    else:
        print("YES")
        print("YES")


if __name__ == "__main__":
    main()
