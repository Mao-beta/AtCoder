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
    sx, sy = NLI()
    gx, gy = NLI()
    XY = [NLI() for _ in range(N)]

    INF = 10**10
    X = defaultdict(lambda: [-INF, INF])
    Y = defaultdict(lambda: [-INF, INF])

    for x, y in XY:
        X[x].append(y)
        Y[y].append(x)

    for L in X.values():
        L.sort()
    for L in Y.values():
        L.sort()

    que = deque()
    que.append((sx, sy, 0))

    seen = set()
    seen.add((sx, sy))

    while que:
        nowx, nowy, step = que.popleft()

        if nowx == gx and nowy == gy:
            print(step)
            exit()

        yidx = bisect.bisect_left(X[nowx], nowy)
        l, r = X[nowx][yidx-1], X[nowx][yidx]

        xidx = bisect.bisect_left(Y[nowy], nowx)
        u, d = Y[nowy][xidx-1], Y[nowy][xidx]

        if l != -INF and l+1 != nowy and (nowx, l+1) not in seen:
            seen.add((nowx, l+1))
            que.append((nowx, l+1, step+1))
        if r != INF and r-1 != nowy and (nowx, r-1) not in seen:
            seen.add((nowx, r-1))
            que.append((nowx, r-1, step+1))
        if u != -INF and u+1 != nowx and (u+1, nowy) not in seen:
            seen.add((u+1, nowy))
            que.append((u+1, nowy, step+1))
        if d != INF and d-1 != nowx and (d-1, nowy) not in seen:
            seen.add((d-1, nowy))
            que.append((d-1, nowy, step+1))

    print(-1)


if __name__ == "__main__":
    main()
