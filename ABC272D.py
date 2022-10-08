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
    N, M = NMI()
    DH = []
    DW = []
    for dh in range(-1000, 1001):
        for dw in range(-1000, 1001):
            if dh**2 + dw**2 == M:
                DH.append(dh)
                DW.append(dw)

    start = (0, 0)

    queue = deque()
    queue.append(start)
    dist = [[-1] * N for _ in range(N)]
    dist[start[0]][start[1]] = 0

    while queue:
        now_h, now_w = queue.popleft()
        now_step = dist[now_h][now_w]

        for dh, dw in zip(DH, DW):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step + 1

            if goto_h < 0 or goto_h >= N or goto_w < 0 or goto_w >= N:
                continue
            if 0 <= dist[goto_h][goto_w] <= goto_step:
                continue

            queue.append((goto_h, goto_w))
            dist[goto_h][goto_w] = goto_step

    for row in dist:
        print(*row)


if __name__ == "__main__":
    main()
