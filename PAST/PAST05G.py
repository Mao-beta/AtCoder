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
    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    X = 0
    for row in S:
        X += row.count("#")


    def rec(h, w):

        seen[h][w] = 1
        ans.append((h+1, w+1))
        if len(ans) == X:
            print(X)
            for row in ans:
                print(*row)
            exit()

        for dh, dw in zip(DH, DW):
            nh = h + dh
            nw = w + dw
            if nh < 0 or nh >= H or nw < 0 or nw >= W:
                continue
            if S[nh][nw] == ".":
                continue
            if seen[nh][nw] == 1:
                continue

            rec(nh, nw)

        seen[h][w] = 0
        if ans:
            ans.pop()


    for sh in range(H):
        for sw in range(W):
            seen = [[0]*W for _ in range(H)]
            ans = []
            if S[sh][sw] == "#":
                rec(sh, sw)



if __name__ == "__main__":
    main()
