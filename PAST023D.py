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
    H, W, c1, c2 = SMI()
    H, W = int(H), int(W)
    S = [SI() for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if S[h][w] != c1:
                continue
            for dh, dw in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                nh, nw = h+dh, w+dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == c2:
                    print("Yes")
                    return
    print("No")


if __name__ == "__main__":
    main()
