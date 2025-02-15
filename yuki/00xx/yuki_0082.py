import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    W, H, C = SMI()
    W = int(W)
    H = int(H)
    ans = [[C] * W for _ in range(H)]
    if C == "B":
        D = "W"
    else:
        D = "B"
    for h in range(H):
        for w in range(W):
            if (h + w) % 2:
                ans[h][w] = D
    for row in ans:
        print("".join(row))


if __name__ == "__main__":
    main()
