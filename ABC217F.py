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
        return self.fac[n] * self.inv[r] % MOD * self.inv[n - r] % MOD

    def perm(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self.fac[n] * self.inv[n - r] % MOD


def main():
    N, M = NMI()
    AB = [NLI() for _ in range(M)]

    C = Combinations(400, MOD)

    # dp[l][r]: [l, r)を除去したときの通りの数
    # ans = dp[0][2*N]
    dp = [[0]*(2*N+1) for _ in range(2*N+1)]

    can_pair = [[0]*(2*N) for _ in range(2*N)]
    for a, b in AB:
        a, b = a-1, b-1
        can_pair[a][b] = 1
        can_pair[b][a] = 1

    for l in range(2*N+1):
        dp[l][l] = 1

    # [l, r)の通りを, r-l=gapの小さい順に考える
    # [l, i), [i, r)に分け、かつlとi-1がペアになるケースを全探索
    # そもそもlとi-1の相性が悪ければ無理
    # このとき[l+1, i-1)の内部と[i, r)の内部は交わらず、各通りで内部ごとの順序は決まっているので、
    # 合成された順序は(全体のペア数から後半のペア数を選ぶ組み合わせ数)倍になる

    # gap: 0...2N, l: 0...2N-gap, r=l+gap
    # lとrのもとで、i: l+1...r

    for gap in range(2*N+1):
        for l in range(0, 2*N+1 - gap):
            r = l + gap
            for i in range(l+1, r+1):
                if not can_pair[l][i-1]:
                    continue
                k = (r-i) // 2
                n = (r-l) // 2
                x = dp[l+1][i-1] * dp[i][r] % MOD * C.cmb(n, k) % MOD
                dp[l][r] += x
            dp[l][r] %= MOD

    print(dp[0][2*N])


if __name__ == "__main__":
    main()
