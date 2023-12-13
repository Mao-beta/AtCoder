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
    N, D = NMI()
    W = NLI()
    INF = 3 * 10 ** 18
    total = sum(W)

    Ys = [0] * (1 << N)
    for s in range(1 << N):
        x = sum(W[i] for i in range(N) if (s >> i) & 1)
        Ys[s] = x

    # dp[d][S]: d袋できて使った集合がSのときの Σ(x_i^2) のmin
    # 最後にD倍してtotal^2を引いてからD^2で割る
    dp = [w ** 2 for w in Ys]

    for d in range(2, D+1):
        dp2 = [INF] * (1 << N)
        for s in range(1 << N):
            dp2[s] = INF
            ns = s
            while ns:
                dp2[s] = min(dp2[s], dp[s ^ ns] + Ys[ns]**2)
                ns = (ns - 1) & s
        dp = dp2

    print((dp[-1]*D - total**2) / D**2)


def main_TLE():
    N, D = NMI()
    W = NLI()
    INF = 3 * 10 ** 18
    total = sum(W)

    Ys = [0] * (1 << N)
    for s in range(1 << N):
        x = sum(W[i] for i in range(N) if (s >> i) & 1)
        Ys[s] = (D * x - total) ** 2

    # dp[d][S]: d袋できて使った集合がSのときの Σ(D*x_i - total)^2 のmin
    # 最後にD^3で割る
    dp = Ys[:]

    for d in range(2, D + 1):
        dp2 = [INF] * (1 << N)
        for s in range(1 << N):
            dp2[s] = INF
            ns = s
            while ns:
                dp2[s] = min(dp2[s], dp[s ^ ns] + Ys[ns])
                ns = (ns - 1) & s
        dp = dp2

    print(dp[-1] / D ** 3)


if __name__ == "__main__":
    main()
