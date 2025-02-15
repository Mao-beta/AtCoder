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
    N, V, sw, sh, gw, gh = NMI()
    H, W = N, N
    L = EI(H)

    if V > 2*N*9:
        ans = abs(sw-gw) + abs(sh-gh)
        print(ans)
        return

    assert V <= 1800
    INF = 10 ** 10
    sw, sh, gw, gh = sw-1, sh-1, gw-1, gh-1

    start = (sh, sw, V)

    queue = deque()
    queue.append(start)

    steps = [[[INF]*(V+1) for _ in range(W)] for _ in range(H)]
    steps[sh][sw][V] = 0

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    while queue:
        now_h, now_w, now_v = queue.popleft()
        now_step = steps[now_h][now_w][now_v]
        if now_h == gh and now_w == gw:
            print(now_step)
            return

        for dh, dw in zip(DH, DW):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step + 1

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue

            goto_v = now_v - L[goto_h][goto_w]
            if goto_v <= 0:
                continue
            if 0 <= steps[goto_h][goto_w][goto_v] <= goto_step:
                continue

            queue.append((goto_h, goto_w, goto_v))
            steps[goto_h][goto_w][goto_v] = goto_step

    print(-1)


if __name__ == "__main__":
    main()
