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
            self.data[p - 1] += x % MOD
            self.data[p - 1] %= MOD
            p += p & -p

    def get(self, p):
        return self.sum(p, p + 1) % MOD

    def sum(self, l, r):
        assert (0 <= l and l <= r and r <= self.n), "0<=l<=r<=n,l={0},r={1},n={2}".format(l, r, self.n)
        return (self.sum0(r) - self.sum0(l)) % MOD

    def sum0(self, r):
        s = 0
        while (r > 0):
            s += self.data[r - 1]
            s %= MOD
            r -= r & -r
        return s

    def debug(self):
        res = [self.get(p) for p in range(self.n)]
        return res


def main():
    N, K = NMI()
    M = int(N ** 0.5)

    # dp[i][j]: i個並べて、最後がj
    dp = BIT(M+1)
    # dp2[i][j]: i個並べて、最後がMより大きい、隣の最大値がjになるもの
    dp2 = BIT(M+1)

    dp.add(1, 1)

    # 次回がj以上になるもの＝最後が N//j 以下
    # 次回が(j+1)以上になるもの＝最後が N//(j+1) 以下
    # 次回の最大値がj ＝ [最後が max(N//(j+1), M+1) < x <= N//j]

    # N=10
    # 1  2 3 4 5 6 7 8 9 10
    # 10 5 3 2 2 1 1 1 1  1

    for i in range(1, K+1):
        ndp = BIT(M+1)
        ndp2 = BIT(M+1)
        for j in range(1, M+1):
            # jを置くとき、
            # dp[i-1][1~M] + dp2[i-1][j~M]までOK
            ndp.add(j, dp.sum(1, M+1) + dp2.sum(j, M+1))

            # 次に最大でjが置けるものを置くとき、
            # dp[i-1][1~j]までOKで、候補は N//j - max(N//(j+1), M+1) 個ある
            k = max(0, N//j - max(N//(j+1), M))
            ndp2.add(j, dp.sum(1, j+1) * k)
        dp, dp2 = ndp, ndp2

    ans = dp.sum(1, M+1) + dp2.sum(1, M+1)
    ans %= MOD
    print(ans)

    # print(*dp, sep="\n")
    # print(*dp2, sep="\n")


if __name__ == "__main__":
    main()
