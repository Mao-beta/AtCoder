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
    H, W, X = NMI()
    P, Q = NMI()
    S = EI(H)
    P -= 1
    Q -= 1
    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]
    now = S[P][Q]
    hq = [[0, P, Q]]
    seen = [[0]*W for _ in range(H)]
    seen[P][Q] = 1
    while hq:
        s, h, w = heappop(hq)
        if s * X >= now:
            break
        now += s
        for dh, dw in zip(DH, DW):
            nh, nw = h+dh, w+dw
            if 0 <= nh < H and 0 <= nw < W and seen[nh][nw] == 0:
                heappush(hq, [S[nh][nw], nh, nw])
                seen[nh][nw] = 1
    print(now)


if __name__ == "__main__":
    main()
