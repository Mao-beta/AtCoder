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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def combination_mod_initialize(n, MOD=10**9+7):
    fac = [1]*(n+1)
    inv = [1]*(n+1)
    for i in range(1, n+1):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = inv[i-1] * pow(i, -1, MOD) % MOD
    return fac, inv

# 二項係数　高速
def combination_mod(n, r, fac, inv, mod=10**9+7):
    return fac[n] * inv[r] * inv[n-r]


def main():
    S = NI()
    fac, inv = combination_mod_initialize(10000, MOD)
    ans = 0
    if S <= 2:
        print(0)
        exit()
    for n in range(1, S//3+1):
        t = S - 3 * n
        ans += combination_mod(t+n-1, t, fac, inv, MOD)
    print(ans%MOD)



if __name__ == "__main__":
    main()