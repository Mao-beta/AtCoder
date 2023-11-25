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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N = NI()
    X = NLI()
    L = NLI()
    # x1-l1 <= k <= xN+l1 を考える
    # 各i,jについて、(xi+xj)/2 をまたぐと順序がかわる
    P = [[X[0]-L[0], -1, -1], [X[-1]+L[0]+1, -2, -2]]
    for i in range(N):
        for j in range(i+1, N):
            x = (X[i] + X[j] + 1) // 2
            P.append([x, i, j])

    P.sort()
    # print(P)
    # x2l[i]: xiがどのLに対応するか
    x2l = [i for i in range(N)]

    ans = 0
    for i in range(len(P)-1):
        xl, il, jl = P[i]
        xr, ir, jr = P[i+1]

        for p, q in enumerate(x2l):
            xp = X[p]
            lq = L[q]
            xl = max(xl, xp-lq)
            xr = min(xr, xp+lq+1)

        ans += max(xr - xl, 0)
        if ir >= 0 and jr >= 0:
            x2l[ir], x2l[jr] = x2l[jr], x2l[ir]

    print(ans)



if __name__ == "__main__":
    main()
