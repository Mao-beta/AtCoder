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


class LazySegTree:
    def __init__(self, v, op, e, mapping, composition, id_):
        n = len(v)
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_
        self._size = 1 << (n - 1).bit_length()
        self._d = [e] * (2 * self._size)
        self._lz = [id_] * 2 * self._size
        for i in range(n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._d[i] = self._op(self._d[2 * i], self._d[2 * i + 1])

    def _gindex(self, l, r):
        l += self._size
        r += self._size
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()
        while r > l:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            l >>= 1
            r >>= 1
        while l:
            yield l
            l >>= 1

    def _propagates(self, *ids):
        for i in reversed(ids):
            f = self._lz[i]
            self._lz[i] = self._id
            self._lz[2 * i] = self._composition(f, self._lz[2 * i])
            self._lz[2 * i + 1] = self._composition(f, self._lz[2 * i + 1])
            self._d[2 * i] = self._mapping(f, self._d[2 * i])
            self._d[2 * i + 1] = self._mapping(f, self._d[2 * i + 1])

    def apply(self, l, r, f):
        (*ids,) = self._gindex(l, r)
        self._propagates(*ids)
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                self._lz[l] = self._composition(f, self._lz[l])
                self._d[l] = self._mapping(f, self._d[l])
                l += 1
            if r & 1:
                self._lz[r - 1] = self._composition(f, self._lz[r - 1])
                self._d[r - 1] = self._mapping(f, self._d[r - 1])
            l >>= 1
            r >>= 1
        for i in ids:
            self._d[i] = self._op(self._d[2 * i], self._d[2 * i + 1])

    def prod(self, l, r):
        self._propagates(*self._gindex(l, r))
        resl = self._e
        resr = self._e
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                resl = self._op(resl, self._d[l])
                l += 1
            if r & 1:
                resr = self._op(self._d[r - 1], resr)
            l >>= 1
            r >>= 1
        return self._op(resl, resr)


# 区間和・個数取得(prod)・区間affine変換(apply)
INF = 1<<60


class D:
    def __init__(self, m, l, r, m0, l0, r0, s):
        self.m, self.l, self.r, self.m0, self.l0, self.r0, self.s = m, l, r, m0, l0, r0, s


def op(x: D, y: D):
    m = max(x.m, y.m, x.r + y.l)
    m0 = max(x.m0, y.m0, x.r0 + y.l0)
    s = x.s + y.s
    l = x.l if x.l < x.s else x.l + y.l
    r = y.r if y.r < y.s else y.r + x.r
    l0 = x.l0 if x.l0 < x.s else x.l0 + y.l0
    r0 = y.r0 if y.r0 < y.s else y.r0 + x.r0
    return D(m, l, r, m0, l0, r0, s)


# opの単位元
E = D(0, 0, 0, 0, 0, 0, 0)


def mapping(f, a: D):
    # f: 作用する、a: 作用される
    if f:
        m, m0 = a.m0, a.m
        l, r, l0, r0 = a.l0, a.r0, a.l, a.r
        s = a.s
        return D(m, l, r, m0, l0, r0, s)

    else:
        return a


def composition(f, g):
    # f(g())
    return f^g


# mappingの単位元
ID = 0


def main():
    N, Q = NMI()
    S = list(map(int, SI()))
    S = [D(1, 1, 1, 0, 0, 0, 1) if s else D(0, 0, 0, 1, 1, 1, 1) for s in S]
    seg = LazySegTree(S, op, E, mapping, composition, ID)

    for _ in range(Q):
        c, L, R = NMI()
        L -= 1
        if c == 1:
            seg.apply(L, R, 1)
        else:
            print(seg.prod(L, R).m)


if __name__ == "__main__":
    main()
