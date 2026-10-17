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
    H, W = NMI()
    grid = [SI() for _ in range(H)]


    def f(x, y, z, w):
        p = x*W + y
        q = z*W + w
        return p * H * W + q

    start = [0, 0]
    goal = [0, 0]
    bag = [0, 0]
    for h in range(H):
        for w in range(W):
            if grid[h][w] == "s":
                start = [h, w]
            if grid[h][w] == "g":
                goal = [h, w]
            if grid[h][w] == "a":
                bag = [h, w]

    INF = 10**10
    queue = deque()
    queue.append((*start, *bag))
    steps = [INF] * H*W*H*W
    steps[f(*start, *bag)] = 0

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        now_h, now_w, bag_h, bag_w = queue.popleft()
        now_step = steps[f(now_h, now_w, bag_h, bag_w)]
        # print(now_h, now_w, bag_h, bag_w)
        # print(steps)

        if bag_h == goal[0] and bag_w == goal[1]:
            print(now_step)
            exit()

        for dh, dw in dirs:
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step + 1

            goto_ah = bag_h
            goto_aw = bag_w

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue

            if goto_h == bag_h and goto_w == bag_w:
                goto_ah += dh
                goto_aw += dw

            if goto_ah < 0 or goto_ah >= H or goto_aw < 0 or goto_aw >= W:
                continue

            if grid[goto_h][goto_w] == "#":
                continue
            if grid[goto_ah][goto_aw] == "#":
                continue

            if 0 <= steps[f(goto_h, goto_w, goto_ah, goto_aw)] <= goto_step:
                continue

            queue.append((goto_h, goto_w, goto_ah, goto_aw))
            steps[f(goto_h, goto_w, goto_ah, goto_aw)] = goto_step

    print(-1)


if __name__ == "__main__":
    main()
