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
    ans = 0
    for h in range(H):
        for w in range(W-1):
            if grid[h][w] == "." and grid[h][w+1] == ".":
                ans += 1
    for h in range(H-1):
        for w in range(W):
            if grid[h][w] == "." and grid[h+1][w] == ".":
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
