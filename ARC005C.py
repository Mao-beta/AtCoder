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
    H, W = NMI()
    C = [SI() for _ in range(H)]
    S = [0, 0]
    G = [0, 0]
    for h in range(H):
        for w in range(W):
            c = C[h][w]
            if c == "s":
                S = [h, w]
            elif c == "g":
                G = [h, w]

    start = (S[0], S[1], 0)

    queue = deque()
    queue.append(start)
    steps = [[[-1] * W for _ in range(H)] for _ in range(3)]
    steps[0][start[0]][start[1]] = 0

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    while queue:
        now_h, now_w, now_b = queue.popleft()
        now_step = steps[now_b][now_h][now_w]

        for dh, dw in zip(DH, DW):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_b = now_b
            goto_step = now_step + 1

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            if C[goto_h][goto_w] == "#":
                goto_b += 1
            if goto_b >= 3:
                continue

            if 0 <= steps[goto_b][goto_h][goto_w] <= goto_step:
                continue

            queue.append((goto_h, goto_w, goto_b))
            steps[goto_b][goto_h][goto_w] = goto_step

    for b in range(3):
        if steps[b][G[0]][G[1]] >= 0:
            print("YES")
            exit()
    print("NO")


if __name__ == "__main__":
    main()
