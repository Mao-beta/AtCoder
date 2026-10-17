import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


def main():
    H, W = NMI()
    S = [SI() for _ in range(H)]
    ans = [[0]*W for _ in range(H)]

    for h in range(H):
        for w in range(W):
            if S[h][w] == ".":
                continue
            for dh in range(-1, 2):
                for dw in range(-1, 2):
                    nh, nw = h+dh, w+dw
                    if 0 <= nh < H and 0 <= nw < W:
                        ans[nh][nw] += 1

    for row in ans:
        print("".join(map(str, row)))


if __name__ == "__main__":
    main()
