import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    H, W = NMI()
    grid = [SI() for _ in range(H)]
    route = [[0]*W for _ in range(H)]
    route[0][0] = 1

    D = [[-1, 0], [0, -1], [-1, -1]]
    cums = [[[0]*W for _ in range(H)] for _ in range(3)] # L, U, LU
    for h in range(H):
        for w in range(W):
            if grid[h][w] == "#": continue
            diff = 0

            for dh, dw in D:
                nh, nw = h+dh, w+dw
                if nh < 0 or nw < 0: continue
                if grid[nh][nw] == "#": continue


                if dh == -1 and dw == 0:
                    cums[0][h][w] = cums[0][nh][nw] + route[nh][nw]
                    cums[0][h][w] %= MOD
                    diff += cums[0][nh][nw] + route[nh][nw]

                elif dh == 0 and dw == -1:
                    cums[1][h][w] = cums[1][nh][nw] + route[nh][nw]
                    cums[1][h][w] %= MOD
                    diff += cums[1][nh][nw] + route[nh][nw]

                else:
                    cums[2][h][w] = cums[2][nh][nw] + route[nh][nw]
                    cums[2][h][w] %= MOD
                    diff += cums[2][nh][nw] + route[nh][nw]
                route[h][w] = diff % MOD
                route[h][w] %= MOD

    print(route[H-1][W-1] % MOD)


if __name__ == "__main__":
    main()
