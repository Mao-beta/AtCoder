import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def combination_mod_initialize(n, MOD=10**9+7):
    fac = [1]*(n+1)
    inv = [1]*(n+1)
    for i in range(1, n+1):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = inv[i-1] * pow(i, MOD-2, MOD) % MOD
    return fac, inv

# 二項係数　高速
def combination_mod(n, r, fac, inv, mod=10**9+7):
    if n < r: return 0
    if n < 0 or r < 0: return 0
    return fac[n] * inv[r] * inv[n-r]


def main():
    N, M, K = NMI()
    if M < N - K:
        print(0)
        exit()

    fac, inv = combination_mod_initialize(10**6 * 2 + 10)
    print((combination_mod(M+N, N, fac, inv) - combination_mod(M+N, N-K-1, fac, inv)) % MOD)


if __name__ == "__main__":
    main()
