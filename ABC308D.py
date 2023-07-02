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
    SS = [SI() for _ in range(H)]

    dic = defaultdict(lambda: -1)
    for i, s in enumerate("snuke"):
        dic[s] = i

    S = []
    for ss in SS:
        ss = [dic[s] for s in ss]
        S.append(ss)


    if S[0][0] != 0:
        print("No")
        exit()

    start = (0, 0, 0)

    queue = deque()
    queue.append(start)
    G = [[-1] * W for _ in range(H)]
    G[start[0]][start[1]] = 0

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    while queue:
        now_h, now_w, now_s = queue.popleft()
        now_step = G[now_h][now_w]

        for dh, dw in zip(DH, DW):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step + 1

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            if S[goto_h][goto_w] != (now_s + 1) % 5:
                continue
            if 0 <= G[goto_h][goto_w] <= goto_step:
                continue

            queue.append((goto_h, goto_w, (now_s + 1) % 5))
            G[goto_h][goto_w] = goto_step

    if G[-1][-1] > 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
