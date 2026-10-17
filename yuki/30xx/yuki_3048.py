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
    X, N = NMI()
    k = (math.isqrt(1+8*abs(X)) - 1) // 2
    # print(X, N, k)
    if N <= k:
        if X > 0:
            X -= N * (N + 1) // 2
        else:
            X += N * (N + 1) // 2
        print(X)
    else:
        if X > 0:
            X -= k * (k+1) // 2
        else:
            X += k * (k+1) // 2
        N -= k
        if N % 2:
            k += 1
            if X > 0:
                X -= k
            else:
                X += k
            N -= 1
        if X > 0:
            X += N // 2
        else:
            X -= N // 2
        print(X)


if __name__ == "__main__":
    main()
