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

    def perm(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self.fac[n] * self.inv[n - r] % MOD


def main():
    N, M = NMI()

    Comb = Combinations(M, MOD)

    # Aは1, 2, ..., Nとする
    # あるiについてAi=Biである集合をPiとすると、その和集合の補集合が答え
    # sames[k] はk個以上一致している場合の数 = M-k P N-k
    sames = [0] * (N+1)
    for k in range(N+1):
        sames[k] = Comb.perm(M-k, N-k)

    ans = 0
    for i in range(N+1):
        ans += sames[i] * Comb.cmb(N, i) * (-1)**i

    ans = ans * Comb.perm(M, N) % MOD
    print(ans)


if __name__ == "__main__":
    main()
