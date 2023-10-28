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


class BIT():
    """
    BIT 0-index  ACL for python
    add(p, x): p番目にxを加算
    get(p): p番目を取得
    sum0(r): [0:r)の和を取得
    sum(l, r): [l:r)の和を取得
    """

    def __init__(self, N):
        self.n = N
        self.data = [0 for i in range(N)]

    def add(self, p, x):
        assert 0 <= p < self.n, "0<=p<n,p={0},n={1}".format(p, self.n)
        p += 1
        while (p <= self.n):
            self.data[p - 1] += x
            self.data[p - 1] %= MOD99
            p += p & -p

    def get(self, p):
        return self.sum(p, p + 1)

    def sum(self, l, r):
        assert (0 <= l and l <= r and r <= self.n), "0<=l<=r<=n,l={0},r={1},n={2}".format(l, r, self.n)
        return (self.sum0(r) - self.sum0(l)) % MOD99

    def sum0(self, r):
        s = 0
        while (r > 0):
            s += self.data[r - 1]
            s %= MOD99
            r -= r & -r
        return s

    def debug(self):
        res = [self.get(p) for p in range(self.n)]
        return res


def main():
    N = NI()
    A = NLI()
    B = NLI()
    M = 3000
    # i個みて直前がj
    dp = [BIT(M+1) for _ in range(N+1)]
    dp[0].add(0, 1)
    for i in range(N):
        a, b = A[i], B[i]
        for j in range(a, b+1):
            dp[i+1].add(j, dp[i].sum0(j+1))

    ans = dp[-1].sum0(M+1)
    print(ans % MOD99)


if __name__ == "__main__":
    main()
