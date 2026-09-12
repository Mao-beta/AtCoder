import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N, L = NMI()
    A = NLI()
    # n枚残っててうちm枚開いててl個ライフが残ってるときの確率
    dp = [[[0.0]*(L+1) for _ in range(2*N+1)] for _ in range(2*N+1)]
    dp[2*N][0][L] = 1.0
    for n in range(2*N, 1, -2):
        for m in range(n):
            for l in range(1, L+1):
                d = dp[n][m][l]
                if d <= 1e-10:
                    continue
                # print(n, m, l, d)
                # 既知
                p = m / (n-m)
                dp[n-2][m-1][l] += d * p
                if n > m+1:
                    # 未知→連続
                    p = (n-2*m) / (n-m) * 1 / (n-m-1)
                    dp[n-2][m][l] += d * p
                    # 未知→既知 からの次で取得
                    if l > 1:
                        p = (n-2*m) / (n-m) * m / (n-m-1)
                        dp[n-2][m][l-1] += d * p
                    else:
                        p = (n-2*m) / (n-m) * m / (n-m-1)
                        dp[n][m][0] += d * p
                    # 未知→未知
                    p = (n-2*m) / (n-m) * (n-2*m-2) / (n-m-1)
                    dp[n][m+2][l-1] += d * p

    # print(dp)
    ans = 0.0
    sa = sum(A)
    for n in range(0, 2*N+1, 2):
        for m in range(n+1):
            for l in range(L+1):
                p = dp[n][m][l]
                if p <= 1e-10:
                    continue
                if l == 0 or n == 0:
                    pair = (2*N-n) // 2
                    ans += sa * pair * p / N

    print(ans)


if __name__ == "__main__":
    main()
