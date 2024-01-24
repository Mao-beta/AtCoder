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
    N, K, P = NMI()
    C = []
    A = []
    for _ in range(N):
        c, *a = NMI()
        C.append(c)
        A.append(a)

    INF = 10**15
    M = 6 ** K
    dp = [[INF] * M for _ in range(N+1)]
    dp[0][0] = 0

    def f(a):
        res = 0
        for x in a:
            res += x
            res *= 6
        res //= 6
        return res

    def g(x):
        res = []
        for _ in range(K):
            res.append(x % 6)
            x //= 6
        return res[::-1]

    def add(x, y):
        res = [min(5, xx+yy) for xx, yy in zip(x, y)]
        return res

    def ok(x):
        res = [xx-P for xx in x]
        return min(res) >= 0


    for i in range(N):
        a = A[i]
        for j in range(M):
            y = g(j)
            if dp[i][j] >= INF:
                continue
            nj = f(add(a, y))
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            dp[i+1][nj] = min(dp[i+1][nj], dp[i][j] + C[i])

    ans = INF
    for j in range(M):
        x = g(j)
        if ok(x):
            ans = min(ans, dp[N][j])

    print(ans if ans < INF else -1)


if __name__ == "__main__":
    main()
