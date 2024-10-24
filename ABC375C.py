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
    N = NI()
    A = [SI() for _ in range(N)]
    B = [["."] * N for _ in range(N)]
    for h in range(N):
        for w in range(N):
            hh = max(h, N-1-h) - N//2
            ww = max(w, N-1-w) - N//2
            m = max(hh, ww)
            r = N//2 - m
            bh, bw = h, w
            for _ in range(r%4):
                bh, bw = bw, N-1-bh
            B[bh][bw] = A[h][w]
    for row in B:
        print("".join(row))


if __name__ == "__main__":
    main()
