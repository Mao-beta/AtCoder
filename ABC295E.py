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


def main(N, M, K, A):

    Z = A.count(0)
    A = [a for a in A if a > 0]
    A.sort()
    # print(A, Z)
    com = Comb(10**5, MOD99)

    # C[x] = P(A_K <= x)
    # x以下がK個以上ある確率
    C = [0] * (M+1)
    for x in range(1, M+1):
        # y: 元々ある1以上x以下の値の数
        y = bisect.bisect_right(A, x)
        over = len(A) - y
        for k in range(K, N-over+1):
            if 0 <= k-y <= Z:
                # print(Z, k-y, x, k-y, M-x, Z-(k-y))
                C[x] += com.C(Z, k-y) * pow(x, k-y, MOD99) * pow(M-x, Z-(k-y), MOD99) % MOD99

    ans = 0
    for x in range(1, M+1):
        p = C[x] - C[x-1]
        ans += x * p % MOD99

    M_inv = pow(M, MOD99-2, MOD99)
    ans *= pow(M_inv, Z, MOD99)
    return ans % MOD99


if __name__ == "__main__":
    N, M, K = NMI()
    A = NLI()
    print(main(N, M, K, A))
    exit()

    from random import randint

    for _ in range(100):
        N = randint(1, 100)
        M = randint(1, 100)
        K = randint(1, N)
        A = [randint(0, M) for _ in range(N)]
        N = M

        print(N, M, K, A)
        main(N, M, K, A)
