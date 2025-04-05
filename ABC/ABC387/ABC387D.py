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
    S = [SI() for _ in range(H)]
    sh, sw = 0, 0
    gh, gw = 0, 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == "S":
                sh, sw = h, w
            if S[h][w] == "G":
                gh, gw = h, w

    queue = deque()
    queue.append((sh, sw, 0))
    queue.append((sh, sw, 1))
    steps = [[[-1] * W for _ in range(H)] for _ in range(2)]
    steps[0][sh][sw] = 0
    steps[1][sh][sw] = 0

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    while queue:
        now_h, now_w, now_tate = queue.popleft()
        now_step = steps[now_tate][now_h][now_w]
        if now_h == gh and now_w == gw:
            print(now_step)
            return

        for dh, dw in zip(DH, DW):
            if now_tate and dw != 0:
                continue
            if not now_tate and dh != 0:
                continue
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step + 1
            goto_tate = now_tate ^ 1

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            if S[goto_h][goto_w] == "#":
                continue
            if 0 <= steps[goto_tate][goto_h][goto_w] <= goto_step:
                continue

            queue.append((goto_h, goto_w, goto_tate))
            steps[goto_tate][goto_h][goto_w] = goto_step

    # print(*steps, sep="\n")
    print(-1)


if __name__ == "__main__":
    main()
