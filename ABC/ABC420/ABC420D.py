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
    A = [SI() for _ in range(H)]
    start = [0, 0, 0]
    for h in range(H):
        for w in range(W):
            if A[h][w] == "S":
                start = [h, w, 0]

    queue = deque()
    queue.append(start)
    steps = [[[-1] * W for _ in range(H)] for _ in range(2)]
    steps[start[2]][start[0]][start[1]] = 0

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    while queue:
        now_h, now_w, now_state = queue.popleft()
        now_step = steps[now_state][now_h][now_w]
        if A[now_h][now_w] == "G":
            print(now_step)
            return

        for dh, dw in zip(DH, DW):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step + 1
            goto_state = now_state

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            if A[goto_h][goto_w] == "#":
                continue
            if now_state == 0 and A[goto_h][goto_w] == "x":
                continue
            if now_state == 1 and A[goto_h][goto_w] == "o":
                continue
            if A[goto_h][goto_w] == "?":
                goto_state = 1 - now_state
            if 0 <= steps[goto_state][goto_h][goto_w] <= goto_step:
                continue

            queue.append((goto_h, goto_w, goto_state))
            steps[goto_state][goto_h][goto_w] = goto_step

    print(-1)



if __name__ == "__main__":
    main()
