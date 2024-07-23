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
    H, W, Y = NMI()
    A = EI(H)
    hq = []
    land = H * W
    heaped = [[0] * W for _ in range(H)]

    def f(a, h, w):
        return a * 1000000 + h * 1000 + w

    def g(f):
        a, hw = divmod(f, 1000000)
        h, w = divmod(hw, 1000)
        return a, h, w

    for h in range(H):
        for w in range(W):
            if h == 0 or h == H-1 or w == 0 or w == W-1:
                heappush(hq, f(A[h][w], h, w))
                heaped[h][w] = 1

    DH = [1, -1, 0, 0]
    DW = [0, 0, 1, -1]
    for y in range(1, Y+1):
        # print("year", y)
        while hq and g(hq[0])[0] <= y:
            l, h, w = g(heappop(hq))
            # print(l, h, w)
            land -= 1
            for dh, dw in zip(DH, DW):
                nh, nw = h+dh, w+dw
                if 0 <= nh < H and 0 <= nw < W:
                    if not heaped[nh][nw]:
                        heappush(hq, f(A[nh][nw], nh, nw))
                        heaped[nh][nw] = 1
        print(land)


if __name__ == "__main__":
    main()
