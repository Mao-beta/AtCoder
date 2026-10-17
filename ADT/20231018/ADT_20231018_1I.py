import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


class Comb:
    """nCrのnもrも10**7くらいまで"""

    def __init__(self, n, mod):
        self.mod = mod
        self.fac = [1] * (n + 1)
        self.inv = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fac[i] = self.fac[i - 1] * i % self.mod
        self.inv[n] = pow(self.fac[n], self.mod - 2, self.mod)
        for i in range(n - 1, 0, -1):
            self.inv[i] = self.inv[i + 1] * (i + 1) % self.mod

    def C(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self.fac[n] * self.inv[r] % self.mod * self.inv[n - r] % self.mod

    def P(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self.fac[n] * self.inv[n - r] % self.mod

    def H(self, n, r):
        """
        n個のものから重複を許してr個取り出す
        """
        return self.C(n + r - 1, r)

    def multi(self, L):
        res = self.fac[sum(L)]
        for l in L:
            res = res * self.inv[l] % self.mod
        return res

def main():
    N, K = NMI()
    com = Comb(100, MOD99)
    ans = [0]
    now = [0] * (N+1)

    P = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            P[i][j] = pow(com.fac[i], j, MOD99)

    def rec(s, nex):
        # 合計s, 次入れるのnex
        if s == N:
            tmp = com.fac[N]
            L = []
            for x, k in enumerate(now):
                if x == 0:
                    continue
                for _ in range(k):
                    tmp = tmp * com.inv[x] % MOD99
                tmp = tmp * com.inv[k] % MOD99
                tmp = tmp * P[x-1][k] % MOD99
                if k > 0:
                    L.append(x)

            lcm = math.lcm(*L)
            ans[0] += pow(lcm, K, MOD99) * tmp % MOD99
            ans[0] %= MOD99
            return

        if s > N:
            return

        if nex > N - s:
            return

        for i in range(N+1):
            ns = s + i * nex
            if ns > N:
                break

            now[nex] += i
            rec(ns, nex+1)
            now[nex] -= i

        return

    rec(0, 1)
    print(ans[0])
    # print(cnt[0])


if __name__ == "__main__":
    main()
