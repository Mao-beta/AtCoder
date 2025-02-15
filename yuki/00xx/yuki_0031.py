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
    N, V = NMI()
    C = NLI()
    X = list(accumulate(C))
    Y = list(range(1, N+1))
    ans = X[-1]
    V -= Y[-1]

    if V <= 0:
        print(ans)
        return

    XY = [[x, y] for x, y in zip(X, Y)]

    from functools import cmp_to_key

    def cmp(a, b):
        ax, ay = a
        bx, by = b
        if ax * by < bx * ay:
            return -1
        elif ax * by > bx * ay:
            return 1
        else:
            if bx > by:
                return -1
            elif bx < by:
                return 1
            else:
                return 0

    XY = sorted(XY, key=cmp_to_key(cmp))
    x, y = XY[-1]
    if V > N**2:
        k = (V - N**2) // y
        ans += k * x
        V -= k * y

    # i個見て量j(<=N**2)あるときの値段の最小値
    INF = 10**20
    dp = [INF]*(V+1)
    dp[0] = 0
    for i in range(N):
        x, y = XY[i]
        for j in range(V+1):
            if dp[j] >= INF:
                continue
            nj = j + y
            nj = min(nj, V)
            dp[nj] = min(dp[nj], dp[j] + x)

    print(ans + dp[V])


if __name__ == "__main__":
    main()
