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
    T = NI()
    for _ in range(T):
        N, D = NMI()
        A = NLI()
        B = NLI()
        X = deque()
        total = 0
        for i, (a, b) in enumerate(zip(A, B)):
            # print(i, a, b, total, X)
            X.append([a, i])
            total += a
            while b > 0:
                x, d = X[0]
                if x > b:
                    X[0][0] -= b
                    total -= b
                    b = 0
                else:
                    b -= x
                    total -= x
                    X.popleft()
            while X and X[0][1] <= i-D:
                x, d = X.popleft()
                total -= x
            # print(X)
        print(total)


if __name__ == "__main__":
    main()
