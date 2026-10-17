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
    N, A, B, C, D = NMI()
    H = B-A+1
    W = D-C+1
    PQ = EI(N)
    PQ = [[x-A, y-C] for x, y in PQ]
    ans = [["." for _ in range(W)] for _ in range(H)]
    Sp = set()
    Sm = set()
    for h, w in PQ:
        Sp.add(h+w)
        Sm.add(h-w)
    for h in range(H):
        for w in range(W):
            if h+w in Sp or h-w in Sm:
                ans[h][w] = "#"
    for row in ans:
        print("".join(row))


if __name__ == "__main__":
    main()
