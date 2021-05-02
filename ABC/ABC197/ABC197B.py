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
    H, W, X, Y = NMI()
    grid = [SI() for _ in range(H)]

    X, Y = X-1, Y-1
    ans = 0
    for h in range(X, -1, -1):
        if grid[h][Y] == "#":
            break
        ans += 1

    for h in range(X, H):
        if grid[h][Y] == "#":
            break
        ans += 1

    for w in range(Y, -1, -1):
        if grid[X][w] == "#":
            break
        ans += 1

    for w in range(Y, W):
        if grid[X][w] == "#":
            break
        ans += 1

    print(ans - 3)


if __name__ == "__main__":
    main()
