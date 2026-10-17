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
    N, X, Y = NMI()
    XY = [NLI() for _ in range(N)]

    H = 410
    W = 410
    G = 205
    X, Y = X+G, Y+G
    XY = [[x+G, y+G] for x, y in XY]
    grid = [["."] * W for _ in range(H)]

    start = (G, G)
    for x, y in XY:
        grid[x][y] = "#"

    queue = deque()
    queue.append(start)
    steps = [[-1] * W for _ in range(H)]
    steps[start[0]][start[1]] = 0

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1)]

    while queue:
        now_h, now_w = queue.popleft()
        now_step = steps[now_h][now_w]
        # print(now_h, now_w, now_step)
        if now_h == X and now_w == Y:
            print(now_step)
            exit()

        for dh, dw in dirs:
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step + 1

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            if 0 <= steps[goto_h][goto_w] <= goto_step:
                continue
            if grid[goto_h][goto_w] == "#":
                continue

            queue.append((goto_h, goto_w))
            steps[goto_h][goto_w] = goto_step

    print(-1)


if __name__ == "__main__":
    main()
