import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def popcount(n):
    return bin(n).count("1")


def main():
    H, W = NMI()
    N = H * W
    grid = [SI() for _ in range(H)]
    DIR = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def i2hw(i):
        return i//W, i%W

    def hw2i(h, w):
        return h*W + w

    def in_grid(h, w):
        return 0 <= h < H and 0 <= w < W


    # dp[i][b] 現在地i 移動済地点の集合b
    # 始点16 * 16 * 2^16 = 2^24 = 1.7 * 10^7
    ans = 0

    # 始点を全探索
    for start in range(N):
        sh, sw = i2hw(start)
        dp = [[0]*(1<<N) for _ in range(N)]
        dp[start][1<<start] = 1

        # bit全探索
        for b in range(1 << N):
            for i in range(N):
                h, w = i2hw(i)
                if grid[h][w] == "#":
                    continue
                if dp[i][b] == 0:
                    continue

                for dh, dw in DIR:
                    nh, nw = h+dh, w+dw
                    ni = hw2i(nh, nw)
                    if not in_grid(nh, nw):
                        continue
                    if grid[nh][nw] == "#":
                        continue
                    if (b>>ni) & 1:
                        continue

                    #print(h, w, nh, nw)
                    nb = b | (1<<ni)

                    dp[ni][nb] += dp[i][b]
                    #print(dp[ni][nb])

        # 始点に隣接する点に至るまでの最長の経路長を調べる
        for b in range((1<<N)-1, -1, -1):
            for dh, dw in DIR:
                nh, nw = sh + dh, sw + dw
                if not in_grid(nh, nw): continue
                if grid[nh][nw] == "#": continue
                ni = hw2i(nh, nw)
                if dp[ni][b]:
                    ans = max(ans, popcount(b))

    #print(*dp, sep="\n")
    # 最長でも2だったら無理なので-1
    print(ans if ans > 2 else -1)


if __name__ == "__main__":
    main()
