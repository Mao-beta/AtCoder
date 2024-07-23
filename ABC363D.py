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
    if N <= 10:
        print(N-1)
        return
    N -= 2
    for k in range(1, 50):
        # k桁の回文数
        h = k // 2
        if k % 2:
            # h=2: 10*01 - 99*99 -> 90 * 10
            # h=3: 100*001 - 999*999 -> 900 * 10
            total = 9 * 10**h
            if N >= total:
                N -= total
                continue
            x, r = divmod(N, 10)
            x += 10**(h-1)
            x = str(x)
            print(x + str(r) + x[::-1])
            return
        else:
            total = 9 * 10**(h-1)
            if N >= total:
                N -= total
                continue
            x = N
            x += 10 ** (h - 1)
            x = str(x)
            print(x + x[::-1])
            return


if __name__ == "__main__":
    main()
