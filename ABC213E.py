import sys
import math
from collections import deque
from heapq import heappop, heappush, heapify

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    H, W = NMI()
    grid = [SI() for _ in range(H)]

    start = (0, 0)

    hq = []
    heapify(hq)
    heappush(hq, (0, *start))
    steps = [[-1] * W for _ in range(H)]
    steps[start[0]][start[1]] = 0

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    jump = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            if abs(i*j) < 4:
                if i == 0 and j == 0:
                    continue
                jump.append((i, j))

    while hq:
        now_step, now_h, now_w = heappop(hq)
        if now_h == H-1 and now_w == W-1:
            print(now_step)
            exit()

        for dh, dw in dirs:
            goto_h = now_h + dh
            goto_w = now_w + dw

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            if grid[goto_h][goto_w] == "#":
                continue
            else:
                goto_step = now_step

            if 0 <= steps[goto_h][goto_w] <= goto_step:
                continue

            heappush(hq, (goto_step, goto_h, goto_w))
            steps[goto_h][goto_w] = goto_step

        for dh, dw in jump:
            goto_h = now_h + dh
            goto_w = now_w + dw

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue

            goto_step = now_step + 1

            if 0 <= steps[goto_h][goto_w] <= goto_step:
                continue

            heappush(hq, (goto_step, goto_h, goto_w))
            steps[goto_h][goto_w] = goto_step





if __name__ == "__main__":
    main()
