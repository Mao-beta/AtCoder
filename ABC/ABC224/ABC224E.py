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
    H, W, N = NMI()
    RCA = [NLI() for i in range(N)]
    AHWI = [[a, x-1, y-1, i] for i, (x, y, a) in enumerate(RCA)]
    HMax = [-1] * H
    WMax = [-1] * W
    INF = 10**15
    AHWI.sort(key=lambda x: -x[0])
    AHWI.append([INF]*4)
    
    ans = [0] * N
    tmp = []
    for i in range(N):
        a, h, w, idx = AHWI[i]
        # print(a, h, w, idx)
        res = max(HMax[h], WMax[w]) + 1
        # print(res)
        tmp.append([h, w, res])
        ans[idx] = res

        if AHWI[i+1][0] != a:
            for h, w, r in tmp:
                HMax[h] = max(HMax[h], r)
                WMax[w] = max(WMax[w], r)
            tmp = []

        # print(HMax)
        # print(WMax)
        # print(tmp)

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
