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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    W, H = NMI()

    G = [SLI() for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if G[h][w] == "s":
                sh, sw = h, w
            if G[h][w] == "g":
                gh, gw = h, w

    start = (sh, sw)

    queue = deque()
    queue.append(start)
    steps = [[-1] * W for _ in range(H)]
    steps[start[0]][start[1]] = 0

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    while queue:
        now_h, now_w = queue.popleft()
        now_step = steps[now_h][now_w]

        for dh, dw in zip(DH, DW):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step + 1

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            if G[goto_h][goto_w] == "1":
                continue
            if 0 <= steps[goto_h][goto_w] <= goto_step:
                continue

            queue.append((goto_h, goto_w))
            steps[goto_h][goto_w] = goto_step

    ans = steps[gh][gw]
    if ans == -1:
        print("Fail")
    else:
        print(ans)


if __name__ == "__main__":
    main()
