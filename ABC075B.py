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
    DH = [-1, -1, -1, 0, 0, 1, 1, 1]
    DW = [-1, 0, 1, -1, 1, -1, 0, 1]
    ans = [["#"]*W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                continue
            res = 0
            for dh, dw in zip(DH, DW):
                nh, nw = h+dh, w+dw
                if 0 <= nh < H and 0 <= nw < W:
                    res += S[nh][nw] == "#"
            ans[h][w] = str(res)
    for a in ans:
        print("".join(a))


if __name__ == "__main__":
    main()
