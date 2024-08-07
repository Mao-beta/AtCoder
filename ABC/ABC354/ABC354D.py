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
    A, B, C, D = NMI()
    A += 10 ** 9
    B += 10 ** 9
    C += 10 ** 9
    D += 10 ** 9

    def calc(X, Y):
        x, xr = divmod(X, 4)
        y, yr = divmod(Y, 2)
        res = 8 * x * y
        if xr == 1:
            res += 3 * y
        elif xr == 2:
            res += 6 * y
        elif xr == 3:
            res += 7 * y
        if yr == 1:
            res += 4 * x
            if xr == 1:
                res += 2
            elif xr == 2:
                res += 3
            elif xr == 3:
                res += 3
        return res

    ans = calc(C, D) - calc(A, D) - calc(C, B) + calc(A, B)
    print(ans)


if __name__ == "__main__":
    main()
