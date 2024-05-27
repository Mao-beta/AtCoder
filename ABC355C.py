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
    N, T = NMI()
    A = NLI()
    # i行目、j列目、左下、右下
    X = [0] * (2*N+2)
    for x in range(1, N*N+1):
        i, j = divmod(x-1, N)
        X[i] += x
        X[N+j] += x
        if i == j:
            X[2*N] += x
        if i + j == N-1:
            X[2*N+1] += x

    for t, a in enumerate(A, start=1):
        i, j = divmod(a-1, N)
        X[i] -= a
        X[N+j] -= a
        if X[i] == 0 or X[N+j] == 0:
            print(t)
            return
        if i == j:
            X[2*N] -= a
            if X[2*N] == 0:
                print(t)
                return
        if i + j == N-1:
            X[2*N+1] -= a
            if X[2*N+1] == 0:
                print(t)
                return
    print(-1)


if __name__ == "__main__":
    main()
