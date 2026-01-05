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
    S = [SI() for _ in range(N)]

    start = (1, 1)

    queue = deque()
    steps = [[[-1]*4 for _ in range(N)]for _ in range(N)]
    for d in range(4):
        steps[start[0]][start[1]][d] = 0
        queue.append([*start, d])
    # URDL
    DH = [-1, 0, 1, 0]
    DW = [0, 1, 0, -1]

    # 右に壁があったら左折できる
    # 前にも右にも壁があったら反転できる
    # AC後追記：後ろに下がる or 左が壁ならその場で壁を向く の方がラク
    while queue:
        now_h, now_w, now_d = queue.popleft()
        now_step = steps[now_h][now_w][now_d]

        for goto_d, (dh, dw) in enumerate(zip(DH, DW)):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step + 1
            if steps[now_h][now_w][now_d] < now_step:
                continue
            # print(now_h, now_w, now_d, goto_h, goto_w, goto_step)
            if S[goto_h][goto_w] == "#":
                continue
            if steps[goto_h][goto_w][goto_d] != -1:
                continue

            if now_d == goto_d:
                queue.append((goto_h, goto_w, goto_d))
                steps[goto_h][goto_w][goto_d] = goto_step
            elif now_d == (goto_d+1) % 4:
                back_h = now_h - dh
                back_w = now_w - dw
                if S[back_h][back_w] != "#":
                    continue
                queue.append((goto_h, goto_w, goto_d))
                steps[goto_h][goto_w][goto_d] = goto_step
            elif now_d == (goto_d+2) % 4:
                back_h = now_h - dh
                back_w = now_w - dw
                if S[back_h][back_w] != "#":
                    continue
                right_h = now_h + DH[(now_d+1) % 4]
                right_w = now_w + DW[(now_d+1) % 4]
                if S[right_h][right_w] != "#":
                    continue
                queue.append((goto_h, goto_w, goto_d))
                steps[goto_h][goto_w][goto_d] = goto_step

    ans = 0
    for h in range(N):
        for w in range(N):
            ans += int(max(steps[h][w]) >= 0)
    print(ans)


if __name__ == "__main__":
    main()
