import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    H, W = NMI()
    grid = [SI() for _ in range(H)]
    DIR = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def in_grid(h, w):
        return 0 <= h < H and 0 <= w < W

    now = set()

    def rec(h, w, sh, sw):
        res = 0

        for dh, dw in DIR:
            nh, nw = h+dh, w+dw
            if not in_grid(nh, nw): continue
            if grid[nh][nw] == "#": continue

            if nh == sh and nw == sw:
                res = max(res, len(now))
                continue
            if (nh, nw) in now: continue

            now.add((nh, nw))
            res = max(res, rec(nh, nw, sh, sw))
            now.discard((nh, nw))

        return res

    ans = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] == "#": continue
            now = set()
            now.add((h, w))
            ans = max(ans, rec(h, w, h, w))

    print(ans if ans > 2 else -1)


if __name__ == "__main__":
    main()
