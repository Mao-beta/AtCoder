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
    H, W, hs, ws = NMI()
    N = NI()
    HW = [NLI() for _ in range(N)]
    Q = NI()
    DL = [SLI() for _ in range(Q)]

    WallsH = defaultdict(list)
    WallsW = defaultdict(list)

    for h, w in HW:
        WallsH[h].append(w)
        WallsW[w].append(h)

    for h in WallsH.keys():
        WallsH[h].append(0)
        WallsH[h].append(W+1)
        WallsH[h].sort()

    for w in WallsW.keys():
        WallsW[w].append(0)
        WallsW[w].append(H+1)
        WallsW[w].sort()

    for d, l in DL:
        l = int(l)
        if d == "L" or d == "R":
            if d == "L":
                l *= -1

            if not WallsH[hs]:
                ws += l

            else:
                idx = bisect.bisect_left(WallsH[hs], ws)
                low = WallsH[hs][idx-1] + 1
                high = WallsH[hs][idx] - 1
                if low <= ws + l <= high:
                    ws += l
                elif l > 0:
                    ws = high
                else:
                    ws = low

        else:
            if d == "U":
                l *= -1

            if not WallsW[ws]:
                hs += l

            else:
                idx = bisect.bisect_left(WallsW[ws], hs)
                low = WallsW[ws][idx - 1] + 1
                high = WallsW[ws][idx] - 1
                if low <= hs + l <= high:
                    hs += l
                elif l > 0:
                    hs = high
                else:
                    hs = low

        if hs <= 0:
            hs = 1
        if hs > H:
            hs = H
        if ws <= 0:
            ws = 1
        if ws > W:
            ws = W
        print(hs, ws)


if __name__ == "__main__":
    main()
