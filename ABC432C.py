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
    N, X, Y = NMI()
    A = sorted(NLI())
    M = Y * A[0]
    g = math.gcd(X, Y)
    Xs = X // g
    Ys = Y // g
    d = Ys - Xs
    kx, ky = 0, A[0]
    ans = ky
    for i in range(1, N):
        kd = A[i] - A[i-1]
        if kd % d:
            print(-1)
            return
        z = kd // d
        kx += z * Ys
        ky -= z * Xs
        # print(i, kd, kx, ky, Xs, Ys, z)
        if ky < 0:
            print(-1)
            return
        ans += ky
    print(ans)


if __name__ == "__main__":
    main()
