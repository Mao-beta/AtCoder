import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    C = [SI() for _ in range(H)]

    for h in range(H):
        for w in range(W):
            if C[h][w] == ".":
                start = [h, w]

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

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            if C[goto_h][goto_w] == "#":
                goto_step = now_step + 1
            else:
                goto_step = now_step

            if 0 <= steps[goto_h][goto_w] <= goto_step:
                continue
            if C[goto_h][goto_w] == "#":
                queue.append((goto_h, goto_w))
            else:
                queue.appendleft((goto_h, goto_w))

            if C[now_h][now_w] == "#" and C[goto_h][goto_w] == ".":
                print(now_step)
                return
            steps[goto_h][goto_w] = goto_step

    print(*steps, sep="\n")


if __name__ == "__main__":
    main()
