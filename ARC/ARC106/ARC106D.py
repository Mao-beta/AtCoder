import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, K = NMI()
    A = [0] + NLI()
    fac = [1]
    inv = [1]
    for i in range(1, 301):
        fac.append(fac[-1] * pow(i, 1, MOD) % MOD)
        inv.append(inv[-1] * pow(i, MOD-2, MOD) % MOD)
    AX = [[0]*(N+1) for k in range(K+1)]
    for k in range(1, K+1):
        for n in range(1, N+1):
            AX[k][n] = AX[k][n-1] + pow(A[n], k, MOD) * inv[k]
        AX[k][0] = 1
    print(AX)

    for x in range(1, K+1):
        S_all_p = 0
        for k in range(x+1):
            S_all_p += AX[x][k] * AX[x][x-k] % MOD
        S_all = fac[x] * S_all_p % MOD

        S_uni = 0
        for n in range(1, N+1):
            S_uni += pow(2*A[n], x, MOD)

        S = (S_all - S_uni) * pow(2, MOD-2, MOD) % MOD
        print(S)



if __name__ == "__main__":
    main()
