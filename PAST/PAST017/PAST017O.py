import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


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
            p += p & -p

    def set(self, p, x):
        self.add(p, -self.get(p))
        self.add(p, x)

    def get(self, p):
        return self.sum(p, p + 1)

    def sum(self, l, r):
        assert (0 <= l and l <= r and r <= self.n), "0<=l<=r<=n,l={0},r={1},n={2}".format(l, r, self.n)
        return self.sum0(r) - self.sum0(l)

    def sum0(self, r):
        s = 0
        while (r > 0):
            s += self.data[r - 1]
            r -= r & -r
        return s

    def debug(self):
        res = [self.get(p) for p in range(self.n)]
        return res


def main():
    N = NI()
    A = NLI()
    Q = NI()
    querys = EI(Q)
    S = set(A)
    B = A[:]
    for q, *X in querys:
        if q == 1:
            k, d = X
            B[k-1] += d
            S.add(B[k-1])
        else:
            S.add(X[0])
    Z, UZ = compress(S)
    ZN = len(Z)
    num_bit = BIT(ZN)
    sum_bit = BIT(ZN)
    for a in A:
        za = Z[a]
        num_bit.add(za, 1)
        sum_bit.add(za, a)
    total = sum(A)
    for q, *X in querys:
        if q == 1:
            k, d = X
            a = A[k-1]
            num_bit.add(Z[a], -1)
            sum_bit.add(Z[a], -a)
            A[k-1] += d
            a = A[k-1]
            num_bit.add(Z[a], 1)
            sum_bit.add(Z[a], a)
            total += d
            # assert num_bit.sum(0, ZN) == N
            # assert sum_bit.sum(0, ZN) == total
        else:
            x = X[0]
            z = Z[x]
            ans = sum_bit.sum(z, ZN) - x * num_bit.sum(z, ZN)
            ans += x * num_bit.sum(0, z) - sum_bit.sum(0, z)
            print(ans)


if __name__ == "__main__":
    main()
