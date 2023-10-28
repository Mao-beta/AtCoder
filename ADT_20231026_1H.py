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
    N = NI()
    Ah, Aw = NMI()
    Bh, Bw = NMI()
    S = [SI() for _ in range(N)]

    start = (Ah-1, Aw-1)

    queue = deque()
    G = [[[-1] * N for _ in range(N)] for _ in range(4)]
    for d in range(4):
        G[d][start[0]][start[1]] = 1
        queue.append((d, *start, 1))

    DH = [1, 1, -1, -1]
    DW = [1, -1, 1, -1]

    while queue:
        now_d, now_h, now_w, now_step = queue.popleft()
        if now_step > G[now_d][now_h][now_w] and G[now_d][now_h][now_w] > 0:
            continue

        G[now_d][now_h][now_w] = now_step

        for di, (dh, dw) in enumerate(zip(DH, DW)):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step + 1
            if di == now_d:
                goto_step -= 1

            if goto_h < 0 or goto_h >= N or goto_w < 0 or goto_w >= N:
                continue
            if S[goto_h][goto_w] == "#":
                continue
            if 0 <= G[now_d][goto_h][goto_w] <= goto_step:
                continue

            if di == now_d:
                queue.appendleft((di, goto_h, goto_w, goto_step))
            else:
                queue.append((di, goto_h, goto_w, goto_step))

    ans = 10**10
    for i in range(4):
        if G[i][Bh - 1][Bw - 1] >= 0:
            ans = min(ans, G[i][Bh-1][Bw-1])
    print(ans if ans < 10**10 else -1)


if __name__ == "__main__":
    main()
