import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    H, W = NMI()
    G = [SI() for _ in range(H)]

    start = (0, 0)

    queue = deque()
    queue.append(start)
    steps = [[-1] * W for _ in range(H)]
    steps[start[0]][start[1]] = 0

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]
    PH = [2, 2, 1, 0, -1, -2, -2, -2, -1, 0, 1, 2, 1, 1, -1, -1]
    PW = [0, -1, -2, -2, -2, -1, 0, 1, 2, 2, 2, 1, 1, -1, 1, -1]

    while queue:
        now_h, now_w = queue.popleft()
        now_step = steps[now_h][now_w]
        if now_h == H-1 and now_w == W-1:
            print(now_step)
            return

        for dh, dw in zip(DH, DW):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            if G[goto_h][goto_w] == "#":
                continue
            if 0 <= steps[goto_h][goto_w] <= goto_step:
                continue

            queue.appendleft((goto_h, goto_w))
            steps[goto_h][goto_w] = goto_step

        for dh, dw in zip(PH, PW):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step + 1

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            if 0 <= steps[goto_h][goto_w] <= goto_step:
                continue

            queue.append((goto_h, goto_w))
            steps[goto_h][goto_w] = goto_step


if __name__ == "__main__":
    main()
