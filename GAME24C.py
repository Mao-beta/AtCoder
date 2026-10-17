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
        A, B, C, D = NMI()
        # Alice: D>C>BB
        # Bob: C>D>AA
        if C >= D:
            C -= D
            D = 0
            C %= 2
            if C == 1:
                B = 2*B+1
                A = 2*A+1
            else:
                B *= 2
                A *= 2
            if B > A:
                print("Alice")
            else:
                print("Bob")
        else:
            D -= C
            C = 0
            D %= 2
            if D == 1:
                B = 2 * B + 1
                A = 2 * A
            else:
                B *= 2
                A *= 2
            if B > A:
                print("Alice")
            else:
                print("Bob")


if __name__ == "__main__":
    main()
