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
    N = NI()
    # RDLU
    DH = [0, 1, 0, -1]
    DW = [1, 0, -1, 0]
    d = 0
    ans = [[0]*N for _ in range(N)]
    ans[0][0] = 1
    ans[N//2][N//2] = "T"
    x = 2
    h, w = 0, 0
    while True:
        dh, dw = DH[d], DW[d]
        nh, nw = h+dh, w+dw
        if nh < 0 or nh >= N or nw < 0 or nw >= N:
            d = (d+1) % 4
            continue
        if ans[nh][nw] == 0:
            ans[nh][nw] = x
            x += 1
            h, w = nh, nw
            continue
        elif ans[nh][nw] == "T":
            break
        else:
            d = (d + 1) % 4

    for row in ans:
        print(*row)


if __name__ == "__main__":
    main()
