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


from typing import List
from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S) -> "List[tuple[int, int]]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


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
    N, M = NMI()
    A = NLI()
    B = NLI()
    A.sort()
    B.sort()

    com = Comb(N+M, MOD99)

    RB = runLengthEncode(B)
    RM = len(RB)

    dp = [[0]*(N+1) for _ in range(RM+1)]
    dp[0][0] = 1
    total = 0

    flg = False
    if RB[-1][0] == max(A+B) and RB[-1][0] > max(A):
        flg = True

    for i in range(RM):
        b, k = RB[i]
        less = bisect.bisect_left(A, b)
        total += k
        for j in range(N+1):
            for x in range(k+1):
                if x > less - j:
                    break
                # x個chmaxする

                if i == RM-1 and flg and x == 0:
                    continue

                if j+x <= total:
                    dp[i+1][j+x] += dp[i][j] * com.C(less-j, x) % MOD99
                    dp[i+1][j+x] %= MOD99

    print(sum(dp[-1]) % MOD99)
    # print(*dp, sep="\n")


if __name__ == "__main__":
    main()
