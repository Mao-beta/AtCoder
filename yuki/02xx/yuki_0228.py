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
    A = EI(4)
    B = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

    DH = [1, -1, 0, 0]
    DW = [0, 0, 1, -1]

    def rec(h, w, state):
        if A == B:
            print("Yes")
            exit()
        for dh, dw in zip(DH, DW):
            nh = h + dh
            nw = w + dw
            if 0 <= nh < 4 and 0 <= nw < 4:
                x = B[nh][nw]
                if (state >> x) & 1:
                    continue
                B[nh][nw], B[h][w] = B[h][w], B[nh][nw]
                rec(nh, nw, state | (1 << x))
                B[nh][nw], B[h][w] = B[h][w], B[nh][nw]

    rec(3, 3, 0)
    print("No")



if __name__ == "__main__":
    main()
