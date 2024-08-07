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
    A = EI(N)
    X = [Counter() for _ in range(N)]
    Y = [Counter() for _ in range(N)]

    for case in range(1<<(N-1)):
        h, w = 0, 0
        x = A[h][w]
        for i in range(N-1):
            if (case >> i) & 1 == 0:
                nh = h + 1
                nw = w
            else:
                nw = w + 1
                nh = h
            x ^= A[nh][nw]
            h, w = nh, nw
        X[w][x] += 1

    for case in range(1 << (N - 1)):
        h, w = N-1, N-1
        x = A[h][w]
        for i in range(N-1):
            if (case >> i) & 1 == 0:
                nh = h - 1
                nw = w
            else:
                nw = w - 1
                nh = h
            x ^= A[nh][nw]
            h, w = nh, nw
        Y[w][x^A[N-1-w][w]] += 1

    ans = 0
    for CX, CY in zip(X, Y):
        for x, k in CX.items():
            ans += CY[x] * k
    print(ans)


if __name__ == "__main__":
    main()
