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
    G = [SI() for _ in range(H)]
    N = NI()
    S = SI()
    DH = [0, 0, 1, -1, 1, 1, -1, -1]
    DW = [1, -1, 0, 0, 1, -1, 1, -1]
    L = set()

    def dfs(h, w, s):
        if s == N:
            return True
        L.add((h, w))
        res = False
        for dh, dw in zip(DH, DW):
            nh = h+dh
            nw = w+dw
            if 0 <= nh < H and 0 <= nw < W:
                if (nh, nw) in L:
                    continue
                if G[nh][nw] == S[s]:
                    res |= dfs(nh, nw, s+1)
        L.discard((h, w))
        return res


    for h in range(H):
        for w in range(W):
            if dfs(h, w, 0):
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    main()
