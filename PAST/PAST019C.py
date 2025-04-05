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
    N = list(map(int, SI()))

    def check(X):
        for i in range(len(X)-1):
            a, b = X[i], X[i + 1]
            if abs(a-b) > 1:
                return False
        return True

    for i in range(len(N)):
        for j in range(10):
            N_ = N[:]
            if i == j == 0:
                res = check(N_)
            else:
                N_[i] = j
                res = check(N_)
            if res:
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    main()
