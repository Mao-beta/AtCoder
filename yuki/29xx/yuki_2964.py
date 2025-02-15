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
    L, K = NMI()
    S = [ord(s)-ord("a") for s in SI()]
    T = [ord(s)-ord("a") for s in SI()]
    A = NLI()
    total = sum(A)
    inv_total = pow(total, MOD99-2, MOD99)

    def f(k, i, j):
        return k * (2*L+1) * L + i * (2*L+1) + j

    # k回やってPNがi, PMがi+jのときの確率
    dp = [0] * ((K+1)*(2*L+1)*L)
    dp[f(0,0,0+L)] = 1
    X = 0
    Y = 0
    for k in range(K):
        for i in range(L):
            for j in range(-L+1, L):
                s = S[i]
                t = T[(i+j)%L]
                d = dp[f(k,i,j+L)]
                if s == t:
                    # c == s == t
                    ni = i + 1
                    nj = i + j + 1 - ni
                    p = A[s] * inv_total % MOD99
                    dp[f(k + 1, ni % L, nj + L)] += d * p % MOD99
                    dp[f(k + 1, ni % L, nj + L)] %= MOD99
                    # else
                    ni = i + 0
                    nj = i + j + 0 - ni
                    p = (total-A[s]) * inv_total % MOD99
                    dp[f(k + 1, ni % L, nj + L)] += d * p % MOD99
                    dp[f(k + 1, ni % L, nj + L)] %= MOD99

                else:
                    # c == s != t
                    ni = i + 1
                    nj = i + j + 0 - ni
                    p = A[s] * inv_total % MOD99
                    dp[f(k + 1, ni % L, nj + L)] += d * p % MOD99
                    dp[f(k + 1, ni % L, nj + L)] %= MOD99
                    # c == t != s
                    ni = i + 0
                    nj = i + j + 1 - ni
                    p = A[t] * inv_total % MOD99
                    dp[f(k + 1, ni % L, nj + L)] += d * p % MOD99
                    dp[f(k + 1, ni % L, nj + L)] %= MOD99
                    # else
                    ni = i + 0
                    nj = i + j + 0 - ni
                    p = (total-A[s]-A[t]) * inv_total % MOD99
                    dp[f(k + 1, ni % L, nj + L)] += d * p % MOD99
                    dp[f(k + 1, ni % L, nj + L)] %= MOD99

    for k in range(K+1):
        for i in range(L):
            X += dp[f(k, i, -L+L)]
            Y += dp[f(k, i, L+L)]
    print(X % MOD99, Y % MOD99)


if __name__ == "__main__":
    main()
