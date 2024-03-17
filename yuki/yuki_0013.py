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
    W, H = NMI()
    M = EI(H)

    steps = [[-1] * W for _ in range(H)]

    for sh in range(H):
        for sw in range(W):
            if steps[sh][sw] >= 0:
                continue


            def bfs(sh, sw):
                x = M[sh][sw]

                queue = deque()
                queue.append([sh, sw, -1, -1])

                steps[sh][sw] = 0

                DH = [0, 0, 1, -1]
                DW = [1, -1, 0, 0]

                while queue:
                    now_h, now_w, prev_h, prev_w = queue.popleft()
                    now_step = steps[now_h][now_w]

                    for dh, dw in zip(DH, DW):
                        goto_h = now_h + dh
                        goto_w = now_w + dw
                        if goto_h == prev_h and goto_w == prev_w:
                            continue

                        goto_step = now_step + 1

                        if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                            continue
                        if M[goto_h][goto_w] != x:
                            continue
                        if 0 <= steps[goto_h][goto_w] <= goto_step:
                            print("possible")
                            exit()

                        queue.append([goto_h, goto_w, now_h, now_w])
                        steps[goto_h][goto_w] = goto_step

            bfs(sh, sw)

    print("impossible")


if __name__ == "__main__":
    main()
