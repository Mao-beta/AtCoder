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
    C = [NLI() for _ in range(H)]

    INF = 10**20
    C[0][0] = INF
    C[-1][-1] = INF

    hq = []
    heapify(hq)
    cost = [[INF] * W for _ in range(H)]
    pars = [[(-1, -1) for _ in range(W)] for _ in range(H)]

    # 右端
    w = W-1
    for h in range(H):
        heappush(hq, (C[h][w], h, w, -1, -1))
        cost[h][w] = C[h][w]

    # 上端
    h = 0
    for w in range(1, H-1):
        heappush(hq, (C[h][w], h, w, -1, -1))
        cost[h][w] = C[h][w]

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)]

    while hq:
        now_cost, now_h, now_w, par_h, par_w = heappop(hq)
        if cost[now_h][now_w] < now_cost:
            continue

        pars[now_h][now_w] = (par_h, par_w)

        for dh, dw in dirs:
            goto_h = now_h + dh
            goto_w = now_w + dw

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue

            goto_cost = now_cost + C[goto_h][goto_w]

            if 0 <= cost[goto_h][goto_w] <= goto_cost:
                continue

            heappush(hq, (goto_cost, goto_h, goto_w, now_h, now_w))
            cost[goto_h][goto_w] = goto_cost

    th, tw = 0, 0
    ans = INF

    w = 0
    for h in range(1, H):
        c = cost[h][w]
        if c < ans:
            ans = c
            th, tw = h, w

    h = H-1
    for w in range(1, W-1):
        c = cost[h][w]
        if c < ans:
            ans = c
            th, tw = h, w

    G = [["."] * W for _ in range(H)]

    while th >= 0 and tw >= 0:
        G[th][tw] = "#"
        th, tw = pars[th][tw]

    print(ans)
    for row in G:
        print("".join(row))


if __name__ == "__main__":
    main()
