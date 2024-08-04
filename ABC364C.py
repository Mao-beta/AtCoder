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
    A = NLI()
    B = NLI()
    A.sort(reverse=True)
    B.sort(reverse=True)
    CA = list(accumulate(A))
    CB = list(accumulate(B))
    ai = bisect.bisect_right(CA, X)
    bi = bisect.bisect_right(CB, Y)
    if ai < N:
        ai += 1
    if bi < N:
        bi += 1
    print(min(ai, bi))


if __name__ == "__main__":
    main()
