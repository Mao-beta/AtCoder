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
    grid = [input() for _ in range(H)]
    L = make_grid(H, W, 0)
    R = make_grid(H, W, 0)
    U = make_grid(H, W, 0)
    D = make_grid(H, W, 0)

    # left
    for h in range(H):
        for w in range(W):
            if grid[h][w] == "#":
                continue
            elif w == 0:
                L[h][w] = 1
            else:
                L[h][w] = L[h][w-1] + 1

    # right
    for h in range(H):
        for w in range(W-1, -1, -1):
            if grid[h][w] == "#":
                continue
            elif w == W-1:
                R[h][w] = 1
            else:
                R[h][w] = R[h][w+1] + 1

    # up
    for w in range(W):
        for h in range(H):
            if grid[h][w] == "#":
                continue
            elif h == 0:
                U[h][w] = 1
            else:
                U[h][w] = U[h-1][w] + 1

    # down
    for w in range(W):
        for h in range(H-1, -1, -1):
            if grid[h][w] == "#":
                continue
            elif h == H-1:
                D[h][w] = 1
            else:
                D[h][w] = D[h+1][w] + 1

    ans = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] == "#":
                continue
            ans = max(ans, L[h][w] + R[h][w] + U[h][w] + D[h][w] - 3)
    print(ans)


if __name__ == "__main__":
    main()