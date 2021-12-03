import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    H, W = NMI()
    S = NLI()
    T = NLI()
    grid = [SI() for _ in range(H)]

    def get_p(h, w, d):
        return h*W + w + H*W*d

    def inv_p(p):
        h, w, d = (p % (H*W))//W, p % W, p // (H*W)
        return h, w, d

    INF = 10**8
    dp = [INF] * (H*W*4)

    queue = deque()
    for d in range(4):
        p = get_p(S[0]-1, S[1]-1, d)
        dp[p] = 0
        queue.append(p)

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        now_p = queue.popleft()
        now_h, now_w, now_d = inv_p(now_p)
        now_turn = dp[now_p]

        if now_h+1 == T[0] and now_w+1 == T[1]:
            print(now_turn)
            exit()

        for goto_d, (dh, dw) in enumerate(dirs):
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_p = get_p(goto_h, goto_w, goto_d)

            if goto_d != now_d:
                goto_turn = now_turn + 1
            else:
                goto_turn = now_turn

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            if 0 <= dp[goto_p] <= goto_turn:
                continue
            if grid[goto_h][goto_w] == "#":
                continue

            if goto_d != now_d:
                queue.append(goto_p)
            else:
                queue.appendleft(goto_p)
            dp[goto_p] = goto_turn


if __name__ == "__main__":
    main()
