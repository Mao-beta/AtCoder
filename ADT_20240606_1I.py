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
    N = SI()
    L = len(N)
    M = NI()
    C = NLI()
    C2b = [-1] * 10
    for i, c in enumerate(C):
        C2b[c] = i
    B = 1 << M
    # dp[k][z][i][j]: i個決めて使った集合がj kは未満確定か zは数字が出てきたか
    dp = [[[[0]*B for _ in range(L+1)] for _ in range(2)] for _ in range(2)]
    for i in range(L):
        n = int(N[i])
        for j in range(B):
            for k in range(2):
                lim = 9 if k else n
                for z in range(2):
                    for x in range(lim+1):
                        ni = i+1
                        nk = k
                        if k == 0 and x < n:
                            nk = 1
                        if z == 0:
                            if x > 0:
                                nz = 1
                            else:
                                nz = 0
                        else:
                            nz = 1

                        b = C2b[x]
                        nj = j
                        if b >= 0:
                            if nz == 0 and x == 0:
                                continue
                            nj = j | (1 << b)

                        if k == 0 and z == 0:
                            continue

                        print(nk, nz, ni, nj, k, z, i, j, x)

                        dp[nk][nz][ni][nj] += dp[k][z][i][j] * 10 + x
                        dp[nk][nz][ni][nj] %= MOD99
    ans = 0
    for k in range(2):
        for z in range(2):
            ans += dp[k][z][-1][-1]
    print(ans % MOD99)


if __name__ == "__main__":
    main()
