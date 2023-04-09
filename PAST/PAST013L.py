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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


class segtree():
    n = 1
    size = 1
    log = 2
    d = [0]
    op = None
    e = 10 ** 15

    def __init__(self, V, OP, E):
        self.n = len(V)
        self.op = OP
        self.e = E
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [E for i in range(2 * self.size)]
        for i in range(self.n):
            self.d[self.size + i] = V[i]
        for i in range(self.size - 1, 0, -1):
            self.update(i)

    def set(self, p, x):
        assert 0 <= p and p < self.n
        p += self.size
        self.d[p] = x
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def get(self, p):
        assert 0 <= p and p < self.n
        return self.d[p + self.size]

    def prod(self, l, r):
        assert 0 <= l and l <= r and r <= self.n
        sml = self.e
        smr = self.e
        l += self.size
        r += self.size
        while (l < r):
            if (l & 1):
                sml = self.op(sml, self.d[l])
                l += 1
            if (r & 1):
                smr = self.op(self.d[r - 1], smr)
                r -= 1
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.d[1]

    def max_right(self, l, f):
        """
        0≤l<Nなる整数 l および条件式 f が与えられたとき、
        f(prod(l,r))=True となる最大の r を求める。
        ただし、与えられる条件式 f は次を満たす:
        ある整数 x>l に対し、f(prod(l,x))=True であるとき、
        任意の整数 l<y≤x について f(prod(l,y))=True である。また、f(e)=True である。
        ->lから右にprodを伸ばしていくとき、はじめて条件がFalseになるrをさがす
        """
        assert 0 <= l and l <= self.n
        assert f(self.e)
        if l == self.n:
            return self.n
        l += self.size
        sm = self.e
        while (1):
            while (l % 2 == 0):
                l >>= 1
            if not (f(self.op(sm, self.d[l]))):
                while (l < self.size):
                    l = 2 * l
                    if f(self.op(sm, self.d[l])):
                        sm = self.op(sm, self.d[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if (l & -l) == l:
                break
        return self.n

    def min_left(self, r, f):
        """
        0≤r<Nなる整数 r および条件式 f が与えられたとき、
        f(prod(l,r))=True となる最小の l を求める。
        ただし、与えられる条件式 f は次を満たす:
        ある整数 x<r に対し、f(prod(x,r))=True であるとき、
        任意の整数 x≤y<r について f(prod(y,r))=True である。また、f(e)=True である。
        ->rから左にprodを伸ばしていくとき、はじめて条件がFalseになるlをさがす
        """
        assert 0 <= r and r < self.n
        assert f(self.e)
        if r == 0:
            return 0
        r += self.size
        sm = self.e
        while (1):
            r -= 1
            while (r > 1 & (r % 2)):
                r >>= 1
            if not (f(self.op(self.d[r], sm))):
                while (r < self.size):
                    r = (2 * r + 1)
                    if f(self.op(self.d[r], sm)):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            if (r & -r) == r:
                break
        return 0

    def update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def __str__(self):
        return str([self.get(i) for i in range(self.n)])


def main():
    N = NI()
    LR = EI(N)
    LR.sort(key=lambda x: (x[0], -x[1]))
    Z, UZ = compress([r for l, r in LR])
    R = [Z[r] for l, r in LR]
    ZN = len(Z)
    seg = segtree([0]*len(Z), max, 0)
    for r in R:
        seg.set(r, seg.prod(r, ZN) + 1)
    print(seg.prod(0, ZN))


if __name__ == "__main__":
    main()
