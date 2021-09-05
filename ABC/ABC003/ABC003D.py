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


class Combinations:
    def __init__(self, n, mod):
        self.mod = mod
        self.fac = [1] * (n + 1)
        self.inv = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fac[i] = self.fac[i - 1] * i % self.mod
            self.inv[i] = self.inv[i - 1] * pow(i, self.mod - 2, self.mod) % self.mod

    def cmb(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self.fac[n] * self.inv[r] * self.inv[n - r] % MOD


def main():
    R, C = NMI()
    X, Y = NMI()
    D, L = NMI()

    Comb = Combinations(1000, MOD)

    def f(x, y):
        if x < 0 or y < 0: return 0
        return Comb.cmb(x*y, D) * Comb.cmb(x*y-D, L) % MOD

    # U...1
    na = f(X, Y)

    # P, Q, R, S...4
    nb = f(X-1, Y) * 2 + f(X, Y-1) * 2

    # 2重複...6
    nc = f(X-1, Y-1) * 4 + f(X-2, Y) + f(X, Y-2)

    # 3重複...4
    nd = f(X-2, Y-1) * 2 + f(X-1, Y-2) * 2

    # 4重複...1
    ne = f(X-2, Y-2)

    ans = na - nb + nc - nd + ne
    ans = ans * (R-X+1) * (C-Y+1) % MOD
    print(ans)


if __name__ == "__main__":
    main()
