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

from operator import add

class LazySegTree:
    __slots__ = [
        "n",
        "log",
        "size",
        "d",
        "lz",
        "e",
        "op",
        "mapping",
        "composition",
        "identity",
    ]

    def _update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def _all_apply(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])

    def _push(self, k):
        if self.lz[k] == self.identity:
            return
        self._all_apply(2 * k, self.lz[k])
        self._all_apply(2 * k + 1, self.lz[k])
        self.lz[k] = self.identity

    def __init__(self, op, e, mapping, composition, id_, v):
        self.n = len(v)
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [e for i in range(2 * self.size)]
        self.lz = [id_ for i in range(self.size)]
        self.e = e
        self.op = op
        self.mapping = mapping
        self.composition = composition
        self.identity = id_
        for i in range(self.n):
            self.d[self.size + i] = v[i]
        for i in range(self.size - 1, 0, -1):
            self._update(i)

    def set(self, p, x):
        assert 0 <= p and p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        self.d[p] = x
        for i in range(1, self.log + 1):
            self._update(p >> i)

    def get(self, p):
        assert 0 <= p and p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        return self.d[p]

    def prod(self, l, r):
        assert 0 <= l and l <= r and r <= self.n
        if l == r:
            return self.e
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push(r >> i)
        sml, smr = self.e, self.e
        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.d[1]

    def apply_point(self, p, f):
        assert 0 <= p and p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        self.d[p] = self.mapping(f, self.d[p])
        for i in range(1, self.log + 1):
            self._update(p >> i)

    def apply(self, l, r, f):
        assert 0 <= l and l <= r and r <= self.n
        if l == r:
            return
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push((r - 1) >> i)
        l2, r2 = l, r
        while l < r:
            if l & 1:
                self._all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self._all_apply(r, f)
            l >>= 1
            r >>= 1
        l, r = l2, r2
        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l:
                self._update(l >> i)
            if ((r >> i) << i) != r:
                self._update((r - 1) >> i)

    def max_right(self, l, g):
        assert 0 <= l and l <= self.n
        assert g(self.e)
        if l == self.n:
            return self.n
        l += self.size
        for i in range(self.log, 0, -1):
            self._push(l >> i)
        sm = self.e
        while 1:
            while i % 2 == 0:
                l >>= 1
            if not (g(self.op(sm, self.d[l]))):
                while l < self.size:
                    self._push(l)
                    l = 2 * l
                    if g(self.op(sm, self.d[l])):
                        sm = self.op(sm, self.d[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if (l & -l) == l:
                break
        return self.n

    def min_left(self, r, g):
        assert 0 <= r and r <= self.n
        assert g(self.e)
        if r == 0:
            return 0
        r += self.size
        for i in range(self.log, 0, -1):
            self._push((r - 1) >> i)
        sm = self.e
        while 1:
            r -= 1
            while r > 1 and (r % 2):
                r >>= 1
            if not (g(self.op(self.d[r], sm))):
                while r < self.size:
                    self._push(r)
                    r = 2 * r + 1
                    if g(self.op(self.d[r], sm)):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            if (r & -r) == r:
                break
        return 0


def AreaOfUnionOfRectangles(recs):
    """
    recs = [(x1, y1, x2, y2), ...]
    returns the area of the union of rectangles
    O(NlogN):  sweep line + lazy segment tree
    """

    # compress the y-coordinates
    ys = set()
    for _, y1, _, y2 in recs:
        ys.add(y1)
        ys.add(y2)
    ys = sorted(ys)
    y2i = {y: i for i, y in enumerate(ys)}

    # transform the rectangles to events
    events = defaultdict(list)
    for x1, y1, x2, y2 in recs:
        events[x1].append((y2i[y1], y2i[y2], 1))
        events[x2].append((y2i[y1], y2i[y2], -1))

    # Initialize the lazy segment tree, support range add and range cnt of none-zero
    BN = 31
    MK = (1 << BN) - 1

    def op(a, b):
        amin, acnt = a >> BN, a & MK
        bmin, bcnt = b >> BN, b & MK
        x, cnt = min(amin, bmin), 0
        if x == amin:
            cnt += acnt
        if x == bmin:
            cnt += bcnt
        return (x << BN) | cnt

    def mapp(f, x):
        return x + (f << BN)

    lst = LazySegTree(
        op=op,
        e=(1 << (2 * BN)) - 1,
        mapping=mapp,
        composition=add,
        id_=0,
        v=[ys[i + 1] - ys[i] for i in range(len(ys) - 1)],
    )

    res, px = 0, min(events)
    N = ys[-1] - ys[0]
    for x in sorted(events):
        dx = x - px
        # for l, r, d in events[x]:
        #     lst.apply(l, r, d)
        val = lst.all_prod()
        vmin, vcnt = val >> BN, val & MK
        if vmin:
            res += dx * N
        else:
            res += dx * (N - vcnt)
        px = x
        for l, r, d in events[x]:
            lst.apply(l, r, d)

    return res


def main():
    H, W, h, w, N = NMI()
    RC = EI(N)
    recs = [(max(0, r-h), max(0, c-w), r, c) for r, c in RC] + [(H-h+1, 0, H, W), (0, W-w+1, H, W)]
    a = AreaOfUnionOfRectangles(recs)
    # print(recs, a)
    print(H * W - a)


if __name__ == "__main__":
    main()
