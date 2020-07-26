import sys
import math
from collections import deque
import heapq as hq

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = NI()
    planes = [list(SI().split()) for _ in range(N)]

    XS = [[] for _ in range(200001)]
    YS = [[] for _ in range(200001)]
    ZS = [[] for _ in range(400001)]
    WS = [[] for _ in range(400001)]
    for plane in planes:
        x, y, u = int(plane[0]), int(plane[1]), plane[2]
        XS[x].append((y, u))
        YS[y].append((x, u))
        ZS[x+y].append((x, u))
        WS[x-y+200000].append((x, u))
    for X in XS:
        hq.heapify(X)
    for Y in YS:
        hq.heapify(Y)
    for Z in ZS:
        hq.heapify(Z)
    for W in WS:
        hq.heapify(W)

    ans = float("inf")

    for X in XS:
        if len(X) <= 1:
            continue
        c = -1
        for _ in range(len(X)):
            k, u = hq.heappop(X)
            if u == "U":
                c = k
            if u == "D" and c >= 0:
                ans = min(ans, (k - c)*5)
                c = -1

    for Y in YS:
        if len(Y) <= 1:
            continue
        c = -1
        for _ in range(len(Y)):
            k, u = hq.heappop(Y)
            if u == "R":
                c = k
            if u == "L" and c >= 0:
                ans = min(ans, (k - c)*5)
                c = -1

    for Z in ZS:
        if len(Z) <= 1:
            continue
        c = -1
        d = -1
        for _ in range(len(Z)):
            k, u = hq.heappop(Z)
            if u == "R":
                c = k
            if u == "D":
                d = k
            if u == "U" and c >= 0:
                ans = min(ans, (k - c)*10)
                c = -1
            if u == "L" and d >= 0:
                ans = min(ans, (k - d)*10)
                d = -1

    for W in WS:
        if len(W) <= 1:
            continue
        c = -1
        d = -1
        for _ in range(len(W)):
            k, u = hq.heappop(W)
            if u == "R":
                c = k
            if u == "U":
                d = k
            if u == "D" and c >= 0:
                ans = min(ans, (k - c)*10)
                c = -1
            if u == "L" and d >= 0:
                ans = min(ans, (k - d)*10)
                d = -1

    if ans == float("inf"):
        print("SAFE")
    else:
        print(ans)


if __name__ == "__main__":
    main()