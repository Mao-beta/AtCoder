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
    H, W, Q = NMI()
    RCX = [SLI() for _ in range(Q)]
    imos = [[0]*W for _ in range(H)]
    for i, (r, c, x) in enumerate(RCX, start=1):
        r, c = int(r), int(c)
        imos[r-1][c-1] = i
    for h in range(H):
        for w in range(W-1, 0, -1):
            imos[h][w-1] = max(imos[h][w-1], imos[h][w])
    for w in range(W):
        for h in range(H-1, 0, -1):
            imos[h-1][w] = max(imos[h-1][w], imos[h][w])
    ans = [["A"]*W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if imos[h][w] > 0:
                ans[h][w] = RCX[imos[h][w]-1][2]
    # print(*imos, sep="\n")
    for row in ans:
        print("".join(row))


if __name__ == "__main__":
    main()
