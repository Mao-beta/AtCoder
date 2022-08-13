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
    XYP = [NLI() for _ in range(N)]

    # i -> j の距離とpi
    D = [[[0, 0] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        xi, yi, pi = XYP[i]
        for j in range(N):
            xj, yj, pj = XYP[j]
            D[i][j][0] = abs(xi-xj) + abs(yi-yj)
            D[i][j][1] = pi

    ok = 10**12
    ng = 0

    while abs(ok - ng) > 1:
        S = (ok + ng) // 2

        ok_flag = False
        for start in range(N):
            seen = [0] * N
            stack = deque()
            stack.append(start)
            seen[start] = 1
            while stack:
                now = stack.pop()
                for j, (d, p) in enumerate(D[now]):
                    if now == j:
                        continue
                    if seen[j]:
                        continue
                    if S * p < d:
                        continue
                    seen[j] = 1
                    stack.append(j)
            if sum(seen) == N:
                ok_flag = True
                break

        if ok_flag:
            ok = S
        else:
            ng = S

    print(ok)


if __name__ == "__main__":
    main()
