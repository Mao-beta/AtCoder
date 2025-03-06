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
    A, B = SMI()

    def f(X):
        N = len(X)
        # i桁見て j:lessで k:最後が1 l:12が何個あったか
        dp = [[[[0]*(N+1) for _ in range(2)] for _ in range(2)] for _ in range(N+1)]
        dp[0][0][0][0] = 1
        for i in range(N):
            s = int(X[i])
            for j in range(2):
                xmax = 9 if j else s
                for k in range(2):
                    for l in range(N+1):
                        d = dp[i][j][k][l]
                        if d == 0:
                            continue
                        for x in range(xmax+1):
                            ni = i+1
                            if j == 0 and x == xmax:
                                nj = 0
                            else:
                                nj = 1
                            nk = 1 if x == 1 else 0
                            nl = l + int(k and x == 2)
                            # print(i, j, k, l, x, ni, nj, nk, nl)
                            dp[ni][nj][nk][nl] += d
        res = 0
        for j in range(2):
            for k in range(2):
                for l in range(N+1):
                    res += dp[N][j][k][l] * l

        if int(X) >= 2:
            res += 1

        if int(X) <= 21:
            return res
        if int(X) <= 99:
            return res + 1

        if int(X[0]) >= 3:
            for i in range(1, N-2+1):
                res += 10**i
            res += 1
        elif int(X[0]) == 2:
            for i in range(1, N - 3 + 1):
                res += 10 ** i
            res += int(X[1:-1]) + 1
            if int(X[-1]) <= 1:
                res -= 1
            res += 1
        else:
            for i in range(1, N-3+1):
                res += 10**i
            res += 1
        return res

    fa = f(str(int(A)-1))
    fb = f(B)
    # print(fa, fb)
    print(fb - fa - int(A[0] == "2" and A[-1] == "2"))


if __name__ == "__main__":
    main()
