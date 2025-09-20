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
    H, W = NMI()
    A = EI(H)
    P = NLI()
    B = [[0]*W for _ in range(H)]
    for h in range(H-1, -1, -1):
        for w in range(W-1, -1, -1):
            if h == H-1 and w == W-1:
                m = 0
            elif h == H-1:
                m = B[h][w+1]
            elif w == W-1:
                m = B[h+1][w]
            else:
                m = min(B[h+1][w], B[h][w+1])
            B[h][w] = max(P[h+w] - A[h][w] + m, 0)
    # m = min(0, B[0][0])
    # h = 0
    # w = 0
    # while h + w < H+W-1:
    #     if h == H-1 and w == W-1:
    #         m = min(m, B[h][w])
    #         break
    #     elif h == H-1:
    #         w += 1
    #     elif w == W-1:
    #         h += 1
    #     elif B[h+1][w] < B[h][w+1]:
    #         h += 1
    #     else:
    #         w += 1
    #     m = min(m, B[h][w])
    # print(*B, sep="\n")
    # print(m)
    # print(B[0][0] - m)
    print(B[0][0])


if __name__ == "__main__":
    main()
