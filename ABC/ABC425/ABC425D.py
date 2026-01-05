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
    S = [list(SI()) for _ in range(H)]




    queue = deque()
    steps = [[-1] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                queue.append((h, w, 0))

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]
    prev_turn = -1
    prev_cells = []

    while queue:
        now_h, now_w, now_turn = queue.popleft()
        now_step = steps[now_h][now_w]
        # print(now_turn, now_h, now_w, now_step, prev_cells)

        if now_turn > prev_turn:
            for h, w in prev_cells:
                S[h][w] = "#"
            prev_turn = now_turn
            prev_cells = []
        # else:
        #     prev_cells.append((now_h, now_w))

        for dh, dw in zip(DH, DW):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step + 1

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            if S[goto_h][goto_w] == "#":
                continue
            if 0 <= steps[goto_h][goto_w] <= goto_step:
                continue
            if steps[goto_h][goto_w] == -2:
                continue

            cnt = 0
            for dh2, dw2 in zip(DH, DW):
                ch = goto_h + dh2
                cw = goto_w + dw2
                if ch < 0 or ch >= H or cw < 0 or cw >= W:
                    continue
                if S[ch][cw] == "#":
                    cnt += 1

            if cnt == 1:
                queue.append((goto_h, goto_w, now_turn+1))
                # S[goto_h][goto_w] = "#"
                steps[goto_h][goto_w] = goto_step
                prev_cells.append((goto_h, goto_w))
            else:
                steps[goto_h][goto_w] = -2

    # print(*steps, sep="\n")
    # print(*S, sep="\n")
    ans = 0
    for row in S:
        ans += row.count("#")
    print(ans)


if __name__ == "__main__":
    main()
