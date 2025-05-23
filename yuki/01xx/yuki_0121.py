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
            p += p & -p

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

    lbit = BIT(ZN)
    rbit = BIT(ZN)
    sbit = BIT(ZN)

    lover = [0] * N
    rover = [0] * N
    lless = [0] * N
    rless = [0] * N
    LC = [0] * N
    RC = [0] * N
    ans = 0

    for a in A:
        RC[a] += 1

    for i, a in enumerate(A):
        lover[i] = lbit.sum(a+1, ZN)
        lless[i] = lbit.sum(0, a)
        lbit.add(a, 1)

        RC[a] -= 1
        ans -= sbit.sum(a+1, ZN)
        ans -= sbit.sum(0, a)
        x = sbit.get(a)
        sbit.add(a, -x)
        LC[a] += 1
        sbit.add(a, LC[a] * RC[a])


    for i, a in enumerate(A[::-1]):
        rover[N-1-i] = rbit.sum(a + 1, ZN)
        rless[N-1-i] = rbit.sum(0, a)
        rbit.add(a, 1)

    for i in range(N):
        ans += lover[i] * rover[i]
        ans += lless[i] * rless[i]

    print(ans)


if __name__ == "__main__":
    main()
