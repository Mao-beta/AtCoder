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
    N, M = NMI()
    DH = [2, 1, -1, -2, -2, -1, 1, 2]
    DW = [1, 2, 2, 1, -1, -2, -2, -1]
    S = set()
    for _ in range(M):
        a, b = NMI()
        for dh, dw in zip(DH, DW):
            nh, nw = a+dh, b+dw
            S.add((a, b))
            if 1 <= nh <= N and 1 <= nw <= N:
                S.add((a+dh, b+dw))
    print(N**2 - len(S))


if __name__ == "__main__":
    main()
