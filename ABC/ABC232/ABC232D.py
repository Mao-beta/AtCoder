import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    H, W = NMI()
    C = [SI() for _ in range(H)]

    DIR = [[1, 0], [0, 1]]

    def i2hw(i):
        return i // W, i % W

    def hw2i(h, w):
        return h * W + w

    def in_grid(h, w):
        return 0 <= h < H and 0 <= w < W


    dp = [[0]*W for _ in range(H)]
    dp[0][0] = 1

    for h in range(H):
        for w in range(W):
            if C[h][w] == "#": continue
            if dp[h][w] == 0: continue

            if h < H-1 and C[h+1][w] != "#":
                dp[h+1][w] = max(dp[h+1][w], dp[h][w]+1)
            if w < W-1 and C[h][w+1] != "#":
                dp[h][w+1] = max(dp[h][w+1], dp[h][w]+1)

    ans = 0
    for row in dp:
        ans = max(ans, max(row))
    print(ans)


if __name__ == "__main__":
    main()
