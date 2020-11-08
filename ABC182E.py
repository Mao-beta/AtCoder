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
    H, W, N, M = NMI()
    lights = [NLI() for _ in range(N)]
    blocks = [NLI() for _ in range(M)]
    grid = make_grid(H, W, 0)
    for h, w in lights:
        grid[h-1][w-1] = 2
    for h, w in blocks:
        grid[h-1][w-1] = 3

    for h in range(H):
        now = 0
        for w in range(W):
            if grid[h][w] == 2:
                now = 1
            elif grid[h][w] == 3:
                now = 0
            else:
                grid[h][w] = max(now, grid[h][w])

        now = 0
        for w in range(W-1, -1, -1):
            if grid[h][w] == 2:
                now = 1
            elif grid[h][w] == 3:
                now = 0
            else:
                grid[h][w] = max(now, grid[h][w])

    for w in range(W):
        now = 0
        for h in range(H):
            if grid[h][w] == 2:
                now = 1
            elif grid[h][w] == 3:
                now = 0
            else:
                grid[h][w] = max(now, grid[h][w])

        now = 0
        for h in range(H-1, -1, -1):
            if grid[h][w] == 2:
                now = 1
            elif grid[h][w] == 3:
                now = 0
            else:
                grid[h][w] = max(now, grid[h][w])

    ans = 0
    for row in grid:
        ans += row.count(1) + row.count(2)
    print(ans)



if __name__ == "__main__":
    main()
