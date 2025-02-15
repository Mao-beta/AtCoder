import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    N, D, K = NMI()
    A = NLI()
    C = NLI()
    INF = 10**15

    def f(j, k):
        return j * (K+1) + k

    # i問見て採用した個数がjで美しさがkのときの満足度のmax
    dp = [-INF] * ((D+1) * (K+1))
    dp2 = [-INF] * ((D+1) * (K+1))
    dp[f(0, 0)] = 0
    for i in range(N):
        for j in range(D+1):
            for k in range(K+1):
                dp2[f(j,k)] = -INF
        a, c = A[i], C[i]
        for j in range(D+1):
            for k in range(K+1):
                d = dp[f(j,k)]
                if d < -INF // 10:
                    continue
                dp2[f(j,k)] = max(dp2[f(j,k)], d)
                if j < D:
                    dp2[f(j+1,min(K, k+c))] = max(dp2[f(j+1,min(K, k+c))], d + a)
        dp, dp2 = dp2, dp
    ans = dp[f(D,K)]
    # print(dp[N])
    print(ans if ans > -INF // 10 else "No")


if __name__ == "__main__":
    main()
