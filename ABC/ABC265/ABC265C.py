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
    G = [SI() for _ in range(H)]

    C = {c:i for i, c in enumerate("UDLR")}
    DH = [-1, 1, 0, 0]
    DW = [0, 0, -1, 1]

    seen = [[0]*W for _ in range(H)]
    h, w = 0, 0
    seen[h][w] = 1

    while True:
        d = C[G[h][w]]
        dh, dw = DH[d], DW[d]
        nh, nw = h+dh, w+dw
        if 0 <= nh < H and 0 <= nw < W:
            if seen[nh][nw]:
                print(-1)
                exit()
            h = nh
            w = nw
            seen[nh][nw] = 1
        else:
            print(h+1, w+1)
            exit()



if __name__ == "__main__":
    main()
