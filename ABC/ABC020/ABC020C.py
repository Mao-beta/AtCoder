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
    H, W, T = NMI()
    S = [SI() for _ in range(H)]

    for h in range(H):
        for w in range(W):
            if S[h][w] == "S":
                start = (h, w)
            if S[h][w] == "G":
                goal = (h, w)

    def judge(X):
        queue = deque()
        queue.append(start)
        steps = [[-1] * W for _ in range(H)]
        steps[start[0]][start[1]] = 0

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            now_h, now_w = queue.popleft()
            now_step = steps[now_h][now_w]

            for dh, dw in dirs:
                goto_h = now_h + dh
                goto_w = now_w + dw
                goto_step = now_step + 1

                if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                    continue
                if S[goto_h][goto_w] == "#":
                    goto_step = now_step + X
                if 0 <= steps[goto_h][goto_w] <= goto_step:
                    continue

                if S[goto_h][goto_w] == "#":
                    queue.append((goto_h, goto_w))
                else:
                    queue.appendleft((goto_h, goto_w))
                steps[goto_h][goto_w] = goto_step

        return steps[goal[0]][goal[1]] <= T

    ok = 1
    ng = 10**9
    while abs(ok - ng) > 1:
        X = (ok + ng) // 2
        if judge(X):
            ok = X
        else:
            ng = X

    print(ok)


if __name__ == "__main__":
    main()
