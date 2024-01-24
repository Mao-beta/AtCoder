import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    S = SI()
    C = Counter(S)
    com = Comb(300000, MOD99)
    ans = 0
    for x in range(K + 1):
        if x > C["A"]:
            break
        for y in range(K + 1):
            if y > C["B"]:
                break
            for z in range(K + 1):
                if z > C["C"]:
                    break
                for k1 in range(x+1):
                    if min(k1, x-k1, y+x-z-k1, z-x+k1, z-y+k1, y-k1) < 0:
                        continue
                    d = min(k1, y+x-z-k1) + min(x-k1, z-y+k1) + min(z-x+k1, y-k1)
                    # if ((x+y+z) - d * 2) % 3:
                    #     continue
                    tmp = d + ((x+y+z) - d * 2) // 3 * 2
                    if tmp <= K:
                        # print(x, y, z, tmp, com.C(C["A"], x), com.C(C["B"], y), com.C(C["C"], z))
                        ans += com.C(C["A"], x) * com.C(C["B"], y) * com.C(C["C"], z) % MOD99
                        ans %= MOD99
    print(ans)


if __name__ == "__main__":
    main()
