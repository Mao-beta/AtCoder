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
    A = [list(SI()) for _ in range(H)]
    
    # RDLU
    DH = [0, 1, 0, -1]
    DW = [1, 0, -1, 0]
    S2d = {s: i for i, s in enumerate(">v<^")}
    S = [0, 0]
    G = [0, 0]
    for h in range(H):
        for w in range(W):
            a = A[h][w]
            if a == "S":
                S = [h, w]
            elif a == "G":
                G = [h, w]
            elif a in ">v<^":
                d = S2d[a]
                dh, dw = DH[d], DW[d]
                nh, nw = h+dh, w+dw
                while 0 <= nh < H and 0 <= nw < W and A[nh][nw] in ".!":
                    A[nh][nw] = "!"
                    nh += dh
                    nw += dw

    start = S

    queue = deque()
    queue.append(start)
    D = [[-1] * W for _ in range(H)]
    D[start[0]][start[1]] = 0

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    while queue:
        now_h, now_w = queue.popleft()
        now_step = D[now_h][now_w]

        for dh, dw in zip(DH, DW):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step + 1

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            if A[goto_h][goto_w] not in "SG.":
                continue
            if 0 <= D[goto_h][goto_w] <= goto_step:
                continue

            queue.append((goto_h, goto_w))
            D[goto_h][goto_w] = goto_step

    ans = D[G[0]][G[1]]
    print(ans if ans >= 0 else -1)


if __name__ == "__main__":
    main()
