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
    N = NI()
    AB = EI(N)

    from functools import cmp_to_key
    def cmp(X, Y):
        xa, xb = X
        ya, yb = Y
        if xa * yb == xb * ya:
            return 0
        elif xa * yb < xb * ya:
            return -1
        else:
            return 1

    AB.sort(key=cmp_to_key(cmp))
    for c, d in AB:
        print(c, d)


if __name__ == "__main__":
    main()
