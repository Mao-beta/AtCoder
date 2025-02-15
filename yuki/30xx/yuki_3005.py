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
    A, B, C, D = EI(4)

    def cross(x, y):
        return x[0]*y[1] - x[1]*y[0]

    def gapped(x, y):
        return x[0]-y[0], x[1]-y[1]

    AB = gapped(B, A)
    AC = gapped(C, A)
    AD = gapped(D, A)
    if cross(AB, AC) * cross(AC, AD) * cross(AD, AB) == 0:
        print("NO")
        return

    def sqrt2(x, y):
        return (x[0]-y[0])**2 + (x[1]-y[1])**2

    def check(a, b, c, d):
        ac2 = sqrt2(a, c)
        bd2 = sqrt2(b, d)
        ab2 = sqrt2(a, b)
        bc2 = sqrt2(b, c)
        cd2 = sqrt2(c, d)
        da2 = sqrt2(d, a)
        return math.isclose(math.sqrt(ac2*bd2), math.sqrt(ab2*cd2) + math.sqrt(bc2*da2))

    for P in permutations([A, B, C, D]):
        if check(*P):
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    main()
