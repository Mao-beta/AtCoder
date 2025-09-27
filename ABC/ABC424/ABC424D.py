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


def solve():
    H, W = NMI()
    S = [list(SI()) for _ in range(H)]
    B = [0] * H

    dp = [[10**9]*(1<<W) for _ in range(H+1)]

    for i in range(H):
        s = 0
        for w in range(W):
            if S[i][w] == "#":
                s += 1<<w
        B[i] = s
    dp[1][B[0]] = 0

    for i in range(1, H):
        for j in range(1<<W):
            if dp[i][j] >= 10**9:
                continue
            # print(i, j, dp[i][j])
            for nj in range(1<<W):
                ok = True
                cnt = 0
                for w in range(W):
                    if (B[i] >> w) & 1 == 0 and (nj >> w) & 1:
                        ok = False
                    if (B[i] >> w) & 1 and (nj >> w) & 1 == 0:
                        cnt += 1
                    if w < W-1 and (j >> w) & 1 and (j >> (w+1)) & 1 and (nj >> w) & 1 and (nj >> (w+1)) & 1:
                        ok = False
                if ok:
                    # print(nj)
                    dp[i+1][nj] = min(dp[i+1][nj], dp[i][j] + cnt)
    # print(*dp, sep="\n")
    print(min(dp[H]))


def main():
    T = NI()
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
