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
    A = NI()
    B = NI()
    C = NI()
    AC = C * pow(A, -1, MOD) % MOD
    BC = C * pow(B, -1, MOD) % MOD
    x = (pow(BC-AC+1, -1, MOD) - 1) % MOD
    y = (BC * (x+1) - 1) % MOD
    print(x, y)


if __name__ == "__main__":
    main()
