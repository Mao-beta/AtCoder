import sys
import math
from collections import defaultdict
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
    return fac[n] * inv[r] * inv[n-r] % mod


def main():
    n, k = NMI()

    fac, inv = combination_mod_initialize(2*n+10)

    if k >= n-1:
        print(combination_mod(2*n-1, n-1, fac, inv))

    else:
        ans = 0
        for z in range(k+1):
            ans += combination_mod(n, z, fac, inv) * combination_mod(n-1, z, fac, inv) % MOD
        print(ans % MOD)


if __name__ == "__main__":
    main()
