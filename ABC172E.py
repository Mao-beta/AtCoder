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



def main():
    N, M = NMI()
    grid = make_grid(N+1, M+1, -1)
    kaizyou = [1]*(M+1)
    for i in range(1, M+1):
        kaizyou[i] = kaizyou[i-1]*i%MOD

    inv = [1]*(M+1)
    for i in range(1, M+1):
        inv[i] = inv[i-1]*pow(i, MOD-2, MOD)%MOD

    def rec(n, m):
        if n == 1:
            return (m-n)%MOD
        if grid[n][m] >= 0:
            return grid[n][m]

        res = rec(n-1, m)*(n-1) + rec(n-1, m-1)*(m-n)
        grid[n][m] = res%MOD
        return res%MOD

    print(rec(N, M) * kaizyou[M] * inv[M-N])

if __name__ == "__main__":
    main()