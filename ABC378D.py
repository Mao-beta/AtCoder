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
    H, W, K = NMI()
    S = [SI() for _ in range(H)]

    DH = [1, -1, 0, 0]
    DW = [0, 0, 1, -1]

    def f(h, w):
        return h*W + w

    def dfs(h, w, k):
        # print(h, w, k, P)
        if k == 0:
            ans[0] += 1
            # print("#")
            return

        for dh, dw in zip(DH, DW):
            nh = h+dh
            nw = w+dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == "." and f(nh, nw) not in P:
                P.add(f(nh, nw))
                dfs(nh, nw, k-1)
                P.discard(f(nh, nw))
        return

    ans = [0]
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                continue
            P = set()
            P.add(f(h, w))
            dfs(h, w, K)
    print(ans[0])


if __name__ == "__main__":
    main()
