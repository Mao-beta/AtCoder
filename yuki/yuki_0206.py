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
    L, M, N = NMI()
    A = NLI()
    B = NLI()
    Q = NI()
    X = 0
    Y = 0
    for a in A:
        X |= 1<<a
    for b in B:
        Y |= 1<<b
    ans = [0] * Q
    for i in range(Q):
        ans[i] = (X&Y).bit_count()
        Y <<= 1
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
