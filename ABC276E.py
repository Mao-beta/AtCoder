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
    G = [SI() for _ in range(H)]

    sx, sy = 0, 0
    for h in range(H):
        for w in range(W):
            if G[h][w] == "S":
                sx, sy = h, w

    start = (sx, sy)

    queue = deque()
    queue.append(start)
    dp = [[-1] * W for _ in range(H)]
    dp[start[0]][start[1]] = 0

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    while queue:
        now_h, now_w = queue.popleft()
        now_step = dp[now_h][now_w]

        for i, (dh, dw) in enumerate(zip(DH, DW)):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step if now_step != 0 else i+1

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            if G[goto_h][goto_w] == "#":
                continue
            if G[goto_h][goto_w] == "S":
                continue
            if dp[goto_h][goto_w] > 0:
                if dp[goto_h][goto_w] == goto_step:
                    continue
                else:
                    print("Yes")
                    exit()

            queue.append((goto_h, goto_w))
            dp[goto_h][goto_w] = goto_step

    print("No")


if __name__ == "__main__":
    main()
