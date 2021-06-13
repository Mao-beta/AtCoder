import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    H, W = NMI()
    grid = [NLI() for _ in range(H)]
    # dp[h][w][k] はh, wまで来た段階でk匹のときの最大値
    dp = [[[0]*(H+W) for _ in range(W+1)] for _ in range(H+1)]

    for h in range(H):
        for w in range(W):
            #print(h, w)
            for k in range(H+W):
                if h < H:
                    if k < H+W-1:
                        dp[h+1][w][k+1] = max(dp[h+1][w][k+1], dp[h][w][k] + grid[h][w])
                    dp[h+1][w][k] = max(dp[h+1][w][k], dp[h][w][k])

                if w < W:
                    if k < H+W-1:
                        dp[h][w+1][k+1] = max(dp[h][w+1][k+1], dp[h][w][k] + grid[h][w])
                    dp[h][w+1][k] = max(dp[h][w+1][k], dp[h][w][k])

    #print(*dp, sep="\n")
    for x in dp[H][W-1][1:]:
        print(x)



if __name__ == "__main__":
    main()
