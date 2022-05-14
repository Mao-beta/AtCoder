import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

sys.setrecursionlimit(10000000)
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
    A = [NLI() for _ in range(H)]
    dp = [[0]*W for _ in range(H)]

    DH = [-1, 0, 1, 0]
    DW = [0, -1, 0, 1]


    def rec(h, w):
        if dp[h][w] > 0:
            return dp[h][w]

        res = 1
        a = A[h][w]

        for dh, dw in zip(DH, DW):
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W:
                if A[nh][nw] > a:
                    if dp[h][w] <= 0:
                        res += rec(nh, nw)
                        res %= MOD

        dp[h][w] = res % MOD
        return res % MOD

    ans = 0
    for h in range(H):
        for w in range(W):
            ans += rec(h, w)
            ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
