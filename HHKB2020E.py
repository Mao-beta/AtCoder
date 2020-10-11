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
    K = sum([g.count(".") for g in grid])
    L = [[0]*W for _ in range(H)]
    for h in range(H):
        now = 1
        for w in range(W):
            if grid[h][w] == "#":
                now = 1
                continue
            L[h][w] += now
            now += 1

    for h in range(H):
        now = 1
        for w in range(W-1, -1, -1):
            if grid[h][w] == "#":
                now = 1
                continue
            L[h][w] += now
            now += 1

    for w in range(W):
        now = 1
        for h in range(H):
            if grid[h][w] == "#":
                now = 1
                continue
            L[h][w] += now
            now += 1

    for w in range(W):
        now = 1
        for h in range(H-1, -1, -1):
            if grid[h][w] == "#":
                now = 1
                continue
            L[h][w] += now
            now += 1

    ans = 0
    for h in range(H):
        for w in range(W):
            if L[h][w] == 0:
                continue
            L[h][w] -= 3
            x = L[h][w]
            ans = ans + pow(2, K-x, MOD)

    ans = K * pow(2, K, MOD) - ans
    print(ans%MOD)



if __name__ == "__main__":
    main()
