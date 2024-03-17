import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    N, H, W = NMI()
    AB = EI(N)
    G = [[0]*W for _ in range(H)]

    def rec(used, total):
        if total == H*W:
            print("Yes")
            exit()

        sh, sw = -1, -1
        for h in range(H):
            for w in range(W):
                if G[h][w] == 0:
                    sh, sw = h, w
                    break
            if sh >= 0:
                break

        for i in range(N):
            if (used >> i) & 1:
                continue
            # check
            a, b = AB[i]
            if total + a*b > H*W:
                continue

            ok = True
            for h in range(sh, sh+a):
                for w in range(sw, sw+b):
                    if h >= H or w >= W or G[h][w] == 1:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                for h in range(sh, sh + a):
                    for w in range(sw, sw + b):
                        G[h][w] = 1
                rec(used | (1<<i), total + a*b)
                for h in range(sh, sh + a):
                    for w in range(sw, sw + b):
                        G[h][w] = 0

            if a == b:
                continue

            a, b = b, a
            ok = True
            for h in range(sh, sh + a):
                for w in range(sw, sw + b):
                    if h >= H or w >= W or G[h][w] == 1:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                for h in range(sh, sh + a):
                    for w in range(sw, sw + b):
                        G[h][w] = 1
                rec(used | (1 << i), total + a*b)
                for h in range(sh, sh + a):
                    for w in range(sw, sw + b):
                        G[h][w] = 0

    rec(0, 0)
    print("No")


if __name__ == "__main__":
    main()
