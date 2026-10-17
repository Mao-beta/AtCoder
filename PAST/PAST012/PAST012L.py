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
    N, M = NMI()
    A = NLI()
    PQLR = EI(M)

    INF = 10**10
    # dp[i][t][m]: i個みて、合計個数mod3がtで、今までの個数mod3がm
    dp = [[[-INF] * 3 for _ in range(3)] for _ in range(N + 1)]
    for t in range(3):
        dp[0][t][0] = 0

    D = [[[0] * 3 for _ in range(3)] for _ in range(N + 1)]
    for p, q, l, r in PQLR:
        t = (l + r) % 3
        if q == 1:
            dp[0][t][0] += p
        else:
            D[q-2][t][l] += p

    # print(*D, sep="\n")

    for i in range(N):
        a = A[i]
        for t in range(3):
            for m in range(3):
                d = dp[i][t][m]
                if d < 0:
                    continue
                # print(i, t, m, d)
                p = D[i][t][(m+1)%3]
                # 使う
                dp[i+1][t][(m+1)%3] = max(dp[i+1][t][(m+1)%3], d + a + p)
                # 使わない
                dp[i+1][t][m] = max(dp[i+1][t][m], d + D[i][t][m])

    ans = 0
    for t in range(3):
        ans = max(ans, dp[-1][t][t])

    # print(*dp, sep="\n")
    print(ans)


if __name__ == "__main__":
    main()
