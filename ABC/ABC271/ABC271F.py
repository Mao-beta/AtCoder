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
    N = NI()
    A = [NLI() for _ in range(N)]

    H = N
    W = N
    que = deque()
    que.append((0, 0, A[0][0]))

    DH = [0, 1]
    DW = [1, 0]

    X = [[] for _ in range(N)]

    while que:
        h, w, x = que.popleft()

        if h + w == N-1:
            X[h].append(x)
            continue

        for dh, dw in zip(DH, DW):
            nh, nw = h+dh, w+dw

            if nh < H and nw < W:
                a = A[nh][nw]
                que.append((nh, nw, x^a))

    # print(X)

    que = deque()
    que.append((N-1, N-1, A[N-1][N-1]))

    DH = [0, -1]
    DW = [-1, 0]

    Y = [[] for _ in range(N)]

    while que:
        h, w, x = que.popleft()
        if h + w == N-1:
            Y[h].append(x^A[h][w])
            continue

        for dh, dw in zip(DH, DW):
            nh, nw = h+dh, w+dw

            if 0 <= nh and 0 <= nw:
                a = A[nh][nw]
                que.append((nh, nw, x^a))

    # print(Y)
    ans = 0

    for x, y in zip(X, Y):
        CX = Counter(x)
        CY = Counter(y)
        for p, k in CX.items():
            ans += k * CY[p]

    print(ans)


if __name__ == "__main__":
    main()
