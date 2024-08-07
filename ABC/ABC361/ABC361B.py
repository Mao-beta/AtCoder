import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    X = NLI()
    Y = NLI()

    def check(xl, xr, yl, yr):
        if yl >= xr or yr <= xl:
            return False
        else:
            return True

    for i in range(3):
        if check(X[i], X[i+3], Y[i], Y[i+3]):
            continue
        print("No")
        return

    print("Yes")


if __name__ == "__main__":
    main()
