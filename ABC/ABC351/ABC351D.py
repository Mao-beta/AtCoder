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
    S = [list(SI()) for _ in range(H)]
    seen = [[-1]*W for _ in range(H)]
    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                continue
            for dh, dw in zip(DH, DW):
                nh, nw = h+dh, w+dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == "#":
                    S[h][w] = "@"

    def bfs(sh, sw):
        c = sh * W + sw
        if S[sh][sw] == "@":
            return 1
        if seen[sh][sw] >= 0 or S[sh][sw] == "#":
            return 0
        res = 0
        que = deque()
        que.append([sh, sw])
        seen[sh][sw] = c

        while que:
            h, w = que.popleft()
            res += 1
            if S[h][w] == "@":
                continue

            for dh, dw in zip(DH, DW):
                nh, nw = h+dh, w+dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] != "#":
                    if seen[nh][nw] == c:
                        continue
                    seen[nh][nw] = c
                    que.append([nh, nw])

        return res

    ans = 0
    for h in range(H):
        for w in range(W):
            ans = max(ans, bfs(h, w))

    print(ans)


if __name__ == "__main__":
    main()
