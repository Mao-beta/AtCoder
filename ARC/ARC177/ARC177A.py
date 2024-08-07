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
    A = NLI()[::-1]
    C = [1, 5, 10, 50, 100, 500][::-1]
    N = NI()
    X = NLI()
    X.sort(reverse=True)
    for x in X:
        for i in range(6):
            a, c = A[i], C[i]
            if a == 0:
                continue
            if x >= c:
                d, r = divmod(x, c)
                d = min(d, a)
                A[i] -= d
                x -= d * c

        if x > 0:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
