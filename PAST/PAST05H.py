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
    H, W = NMI()
    r, c = NMI()
    S = [SI() for _ in range(H)]
    r, c = r-1, c-1

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]
    DM = ["<", ">", "^", "v"]

    G = [[] for _ in range(H*W)]


    def hw2i(h, w):
        return h * W + w

    def i2hw(i):
        return i // W, i % W


    ans = [["x"]*W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                ans[h][w] = "#"
                continue

            i = hw2i(h, w)

            for dh, dw, dm in zip(DH, DW, DM):
                nh = h + dh
                nw = w + dw
                if nh < 0 or nh >= H or nw < 0 or nw >= W:
                    continue

                ns = S[nh][nw]
                ni = hw2i(nh, nw)

                if ns == "#":
                    continue
                elif ns == "." or ns == dm:
                    G[i].append(ni)


    que = deque()
    que.append((r, c))
    ans[r][c] = "o"

    while que:
        h, w = que.popleft()
        i = hw2i(h, w)

        for ni in G[i]:
            nh, nw = i2hw(ni)
            if ans[nh][nw] != "x": continue
            ans[nh][nw] = "o"
            que.append((nh, nw))

    for row in ans:
        print("".join(row))


if __name__ == "__main__":
    main()
