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
    B = [1<<i for i in range(30)]
    X = []

    def rec(now: str):
        for b in B:
            nx = now + str(b)
            if len(nx) <= 9:
                X.append(int(nx))
                rec(nx)

    rec("")
    X = sorted(list(set(X)))
    print(X[N-1])


if __name__ == "__main__":
    main()
