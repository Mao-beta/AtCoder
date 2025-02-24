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
    Tx, Ty, Vt = NMI()
    Ax, Ay, Va = NMI()

    a = Va**2 - Vt**2
    b = Va**2 * Ty - Vt**2 * Ay
    c = Va**2 * (Tx**2 + Ty**2) - Vt**2 * (Ax**2 + Ay**2)
    if a < 0:
        print("inf")
    elif a == 0:
        if b == 0:
            if c <= 0:
                print("inf")
            else:
                print(0)
        else:
            print("inf")
    else:
        d = b**2 - a*c
        if d <= 0:
            print(0)
        else:
            g = 2 * math.sqrt(d) / a
            print(g)


if __name__ == "__main__":
    main()
