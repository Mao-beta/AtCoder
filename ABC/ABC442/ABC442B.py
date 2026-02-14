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
    Q = NI()
    V = 0
    ison = False
    for _ in range(Q):
        A = NI()
        if A == 1:
            V += 1
        elif A == 2:
            if V > 0:
                V -= 1
        else:
            ison = not ison
        if ison and V >= 3:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
