import sys
import math
from collections import defaultdict
from collections import deque
from decimal import Decimal

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def bfs(start, goal, grid, max_turn):
    H = len(grid)
    W = len(grid[0])
    queue = deque()
    queue.append(start)
    steps = [[-1] * W for _ in range(H)]
    steps[start[0]][start[1]] = 0

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        now_h, now_w = queue.popleft()
        now_step = steps[now_h][now_w]

        for dh, dw in dirs:
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step + 1

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            if 0 <= steps[goto_h][goto_w] <= goto_step:
                continue
            if max_turn[grid[goto_h][goto_w]] < goto_step:
                continue
            queue.append((goto_h, goto_w))
            steps[goto_h][goto_w] = goto_step
            if (goto_h, goto_w) == goal:
                return True

    return False


def main():
    N, M = NMI()
    grid = [list(SI()) for _ in range(N)]

    for h, row in enumerate(grid):
        for w, s in enumerate(row):
            if s == "s":
                start = (h, w)
                grid[h][w] = 10
            elif s == "g":
                goal = (h, w)
                grid[h][w] = 10
            elif s == "#":
                grid[h][w] = 0
            else:
                grid[h][w] = int(s)

    # にぶたん
    ok = 1e-10
    ng = 10
    for _ in range(100):
        mid = (ok + ng) / 2
        max_turn = [-1]+[int(math.floor(math.log(mid/i, 0.99) + 0.00000001)) for i in range(1, 10)]+[10000000]

        if bfs(start, goal, grid, max_turn):
            ok = mid
        else:
            ng = mid

    print(ok)



if __name__ == "__main__":
    main()
