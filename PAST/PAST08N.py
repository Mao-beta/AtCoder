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
            self.data[p - 1] += x
            self.data[p - 1] %= MOD
            p += p & -p

    def get(self, p):
        return self.sum(p, p + 1)

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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N = NI()
    A = NLI()
    Z, UZ = compress(A)
    A = [Z[a] for a in A]
    ZN = len(Z)
    # dp_low[i]: 最後がiでかつ底であるような列の数
    # dp_high[i]: 最後がiでかつ天井であるような列の数
    dp_low = BIT(ZN+1)
    dp_high = BIT(ZN+1)
    for a in A:
        dp_low.add(a, dp_high.sum(a+1, ZN+1) + 1)
        dp_high.add(a, dp_low.sum(0, a) + 1)

    ans = dp_high.sum(0, ZN+1) + dp_low.sum(0, ZN+1) - 2 * N
    print(ans % MOD)


if __name__ == "__main__":
    main()
