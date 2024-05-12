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
    N = NI()
    G = [SI() for _ in range(N)]

    def bfs(start, goal, ok_color, ng_color):
        queue = deque()
        queue.append(start)
        steps = [[-1] * N for _ in range(N)]
        steps[start[0]][start[1]] = 0

        DH = [0, 0, 1, -1]
        DW = [1, -1, 0, 0]

        while queue:
            now_h, now_w = queue.popleft()
            now_step = steps[now_h][now_w]

            for dh, dw in zip(DH, DW):
                goto_h = now_h + dh
                goto_w = now_w + dw

                if goto_h < 0 or goto_h >= N or goto_w < 0 or goto_w >= N:
                    continue
                if G[goto_h][goto_w] == ng_color:
                    goto_step = now_step + 1
                else:
                    goto_step = now_step
                if 0 <= steps[goto_h][goto_w] <= goto_step:
                    continue

                if G[goto_h][goto_w] == ng_color:
                    queue.append((goto_h, goto_w))
                else:
                    queue.appendleft((goto_h, goto_w))
                steps[goto_h][goto_w] = goto_step

        return steps[goal[0]][goal[1]]

    r = bfs((0, 0), (N-1, N-1), "R", "B")
    b = bfs((0, N-1), (N-1, 0), "B", "R")
    print(r + b)


if __name__ == "__main__":
    main()
