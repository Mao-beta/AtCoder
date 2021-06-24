import sys
import math
from collections import Counter

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
    N = NI()
    A = NLI()
    d = Counter(A).most_common(1)[0][0]

    if N == 1:
        print(1)
        print(1)
        exit()

    L, M, R = 0, 0, 0
    flg = 0
    for a in A:
        if a == d:
            flg += 1
        else:
            if flg == 0:
                L += 1
            elif flg == 1:
                M += 1
            else:
                R += 1

    fac, inv = combination_mod_initialize(10**5 + 10)

    for k in range(1, N+2):
        if k == 1:
            print(N)
            continue

        ans = combination_mod(N-1, k, fac, inv, MOD)
        ans += combination_mod(N-1, k-1, fac, inv, MOD) * 2 - combination_mod(L+R, k-1, fac, inv, MOD)
        ans += combination_mod(N-1, k-2, fac, inv, MOD)
        print(ans % MOD)




if __name__ == "__main__":
    main()
