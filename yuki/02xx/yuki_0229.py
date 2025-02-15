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

from fractions import Fraction

def main():
    T1 = NI()
    T2 = NI()
    T3 = NI()
    L = T1 * T2 * T3
    V1 = L // T1
    V2 = L // T2
    V3 = L // T3
    # print(L, V1, V2, V3)
    T12 = Fraction(L, (V1+V2))
    T23 = Fraction(L, (V2+V3))
    M12 = Fraction(L, (V1-V2))
    M23 = Fraction(L, (V2-V3))

    def calc(x, y):
        nu = math.lcm(x.numerator, y.numerator)
        de = math.gcd(x.denominator, y.denominator)
        return Fraction(nu, de)

    f = min(calc(T12, T23), calc(M12, M23), calc(T12, M23), calc(T23, M12))
    print(f"{f.numerator}/{f.denominator}")


if __name__ == "__main__":
    main()
