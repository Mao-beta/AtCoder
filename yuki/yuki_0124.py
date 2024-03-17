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
    M = EI(H)

    # h, w, d
    queue = deque()
    queue.append([0, 1, 0])
    queue.append([1, 0, 2])
    steps = [[[10**10]*4 for _ in range(W)] for _ in range(H)]
    steps[0][1][0] = 1
    steps[1][0][2] = 1

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    while queue:
        now_h, now_w, now_d = queue.popleft()
        now_step = steps[now_h][now_w][now_d]
        now = M[now_h][now_w]
        prev_h = now_h - DH[now_d]
        prev_w = now_w - DW[now_d]
        prev = M[prev_h][prev_w]

        for d, (dh, dw) in enumerate(zip(DH, DW)):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_d = d
            goto_step = now_step + 1

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            goto = M[goto_h][goto_w]
            if goto == now or goto == prev:
                continue
            if prev < now < goto or prev > now > goto:
                continue
            if 0 <= steps[goto_h][goto_w][goto_d] <= goto_step:
                continue

            queue.append((goto_h, goto_w, goto_d))
            steps[goto_h][goto_w][goto_d] = goto_step

    ans = min(steps[H-1][W-1])
    if ans >= 10**10:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
