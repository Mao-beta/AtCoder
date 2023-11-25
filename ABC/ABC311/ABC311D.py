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
    S = [SI() for _ in range(H)]

    # URDL: 0123
    # bfs
    queue = deque()
    queue.append((1, 1, 1))
    queue.append((1, 1, 2))
    steps = [[[-1] * W for _ in range(H)] for _ in range(4)]
    for d in range(4):
        steps[d][1][1] = 0

    DH = [-1, 0, 1, 0]
    DW = [0, 1, 0, -1]

    while queue:
        now_h, now_w, now_d = queue.popleft()
        now_step = steps[now_d][now_h][now_w]
        # print(now_h, now_w, now_d)

        dh, dw = DH[now_d], DW[now_d]
        goto_h = now_h + dh
        goto_w = now_w + dw
        goto_d = now_d
        goto_step = now_step + 1

        if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
            continue
        if S[goto_h][goto_w] == "#":
            for d in range(4):
                if steps[d][now_h][now_w] < 0:
                    queue.append((now_h, now_w, d))
                    steps[d][now_h][now_w] = goto_step
            continue
        if 0 <= steps[goto_d][goto_h][goto_w] <= goto_step:
            continue

        queue.append((goto_h, goto_w, goto_d))
        steps[goto_d][goto_h][goto_w] = goto_step

    ans = 0
    for h in range(H):
        for w in range(W):
            ok = False
            for d in range(4):
                if steps[d][h][w] >= 0:
                    ok = True
            if ok:
                ans += 1

    print(ans)

    # for d in range(4):
    #     print(*steps[d], sep="\n")


if __name__ == "__main__":
    main()
