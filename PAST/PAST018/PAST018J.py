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
    S = [SI() for _ in range(H)]
    INF = 10**10

    def f(state, nh, nw):
        return state ^ (1 << (nh*W+nw))

    ns = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                ns = f(ns, h, w)

    dp = [[[INF]*(1<<(H*W)) for _ in range(W)] for _ in range(H)]
    dp[0][0][ns] = 0
    que = deque()
    que.append((0, 0, ns))
    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    while que:
        h, w, s = que.popleft()
        for dh, dw in zip(DH, DW):
            nh, nw = h+dh, w+dw
            if nh < 0 or nw < 0 or nh >= H or nw >= W:
                continue
            ns = f(s, nh, nw)
            if dp[nh][nw][ns] < INF:
                continue
            dp[nh][nw][ns] = dp[h][w][s] + 1
            que.append((nh, nw, ns))

    ans = INF
    for h in range(H):
        for w in range(W):
            ans = min(ans, dp[h][w][0])
    print(ans)


if __name__ == "__main__":
    main()
