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
    T, H, W, i0 = NMI()
    walls_s = [SI() for _ in range(H-1)]
    walls_e = [SI() for _ in range(H)]
    K = NI()
    SD = EI(K)

    def f(h, w):
        return h * W + w

    def g(idx):
        return divmod(idx, W)

    start = (i0, 0)

    queue = deque()
    queue.append(start)
    steps = [[-1] * W for _ in range(H)]
    steps[start[0]][start[1]] = 0

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    pars = [-1] * (H*W)

    def check_goto(goto_h, goto_w, dh, dw):
        if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
            return False
        if dh == 1 and walls_s[goto_h-1][goto_w] == "1":
            return False
        elif dh == -1 and walls_s[goto_h][goto_w] == "1":
            return False
        elif dw == 1 and walls_e[goto_h][goto_w-1] == "1":
            return False
        elif dw == -1 and walls_e[goto_h][goto_w] == "1":
            return False
        return True

    orders = []

    while queue:
        now_h, now_w = queue.popleft()
        now_idx = f(now_h, now_w)
        orders.append(now_idx)
        now_step = steps[now_h][now_w]

        for dh, dw in zip(DH, DW):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_idx = f(goto_h, goto_w)
            goto_step = now_step + 1

            if not check_goto(goto_h, goto_w, dh, dw):
                continue

            if 0 <= steps[goto_h][goto_w] <= goto_step:
                continue

            queue.append((goto_h, goto_w))
            steps[goto_h][goto_w] = goto_step
            pars[goto_idx] = now_idx

    rem = set(range(H*W))
    # -1:通路
    status = [[0]*W for _ in range(H)]

    s_idx = f(i0, 0)

    for r in orders[::-1]:
        if r not in rem:
            continue
        # print("start", g(r))
        prev_h, prev_w = g(r)
        r = pars[r]
        finish = False

        while r != -1:
            now_h, now_w = g(r)
            if status[now_h][now_w] == 9:
                break
            # print("9,", g(r), prev_h, prev_w)
            status[now_h][now_w] = 9

            for dh, dw in zip(DH, DW):
                goto_h = now_h + dh
                goto_w = now_w + dw
                goto_idx = f(goto_h, goto_w)

                if not check_goto(goto_h, goto_w, dh, dw):
                    continue

                rem.discard(goto_idx)

                if goto_h != prev_h and goto_w != prev_w:
                    if status[goto_h][goto_w] == 9:
                        finish = True

            if finish:
                # print("f")
                break
            r = pars[r]
            prev_h, prev_w = now_h, now_w

    # for h in range(H):
    #     for w in range(W):
    #         ok = True
    #         for dh, dw in zip(DH, DW):
    #             goto_h = h + dh
    #             goto_w = w + dw
    #             goto_idx = f(goto_h, goto_w)
    #
    #             if not check_goto(goto_h, goto_w, dh, dw):
    #                 ok = False
    #                 continue
    #             if status[goto_h][goto_w] == 0:
    #                 ok = False
    #                 continue
    #
    #         if ok and status[h][w] == 9:
    #             status[h][w] = 0

    SD = [(s, d, i) for i, (s, d) in enumerate(SD, start=1)]
    SD.sort(key=lambda x: -(x[1] - x[0]))
    valids = []
    for h in range(H):
        for w in range(W):
            if status[h][w] == 0:
                valids.append((h, w))

    ans = []
    SD = set(SD)
    for h, w in valids:
        tmp = []
        for s, d, i in list(SD):
            ok = True
            for ss, dd, ii in tmp:
                if not (d < ss or dd < s):
                    ok = False
            if ok:
                tmp.append([s, d, i])
                ans.append([i, h, w, s])
                SD.discard((s, d, i))
        # print(tmp)

    print(len(ans))
    for row in ans:
        print(*row)


if __name__ == "__main__":
    main()
