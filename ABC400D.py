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
    A, B, C, D = NMI()
    A, B, C, D = A - 1, B - 1, C - 1, D - 1
    hq = deque()
    hq.append([0, A, B])
    INF = 10**10
    steps = [[INF]*W for _ in range(H)]
    steps[A][B] = 0
    while hq:
        cost, x, y = hq.popleft()
        if steps[x][y] < cost:
            continue
        # print(cost, x, y)
        if x == C and y == D:
            print(cost)
            exit()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < H and 0 <= ny < W):
                continue
            if S[nx][ny] == ".":
                nc = cost
                if steps[nx][ny] <= nc:
                    continue
                hq.appendleft([nc, nx, ny])
                steps[nx][ny] = nc
            else:
                nc = cost + 1
                if steps[nx][ny] <= nc:
                    continue
                hq.append([nc, nx, ny])
                steps[nx][ny] = nc
        for dx, dy in [[2, 0], [-2, 0], [0, 2], [0, -2]]:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < H and 0 <= ny < W):
                continue
            if S[nx][ny] == "#":
                nc = cost + 1
                if steps[nx][ny] <= nc:
                    continue
                hq.append([nc, nx, ny])
                steps[nx][ny] = nc


if __name__ == "__main__":
    main()
