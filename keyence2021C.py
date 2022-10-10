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
    H, W, K = NMI()
    dp = [[0]*W for _ in range(H)]
    dp[0][0] = pow(3, H*W-K, MOD99)
    inv3 = pow(3, MOD99-2, MOD99)

    R = [[""]*W for _ in range(H)]
    for _ in range(K):
        h, w, c = SMI()
        h, w = int(h) - 1, int(w) - 1
        R[h][w] = c

    for h in range(H):
        for w in range(W):
            c = R[h][w]
            now = dp[h][w]
            bh, bw = 0, 0

            if c == "":
                bh, bw = 2, 2
                now = now * inv3 % MOD99
            elif c == "X":
                bh, bw = 1, 1
            elif c == "R":
                bh, bw = 0, 1
            elif c == "D":
                bh, bw = 1, 0

            if h < H-1:
                dp[h+1][w] += now * bh
                dp[h+1][w] %= MOD99
            if w < W-1:
                dp[h][w+1] += now * bw
                dp[h][w+1] %= MOD99

    # print(*R, sep="\n")
    # print(*dp, sep="\n")
    print(dp[-1][-1])


if __name__ == "__main__":
    main()
