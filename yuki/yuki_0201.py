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


sys.set_int_max_str_digits(10**6)

def main():
    a, x, _ = SLI()
    b, y, _ = SLI()
    x, y = int(x), int(y)
    if x > y:
        print(a)
    elif x < y:
        print(b)
    else:
        print(-1)


if __name__ == "__main__":
    main()
