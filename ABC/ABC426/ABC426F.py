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


class _SegmentTreeBeats:
    POS_INF = 1 << 60  # float("inf")
    NEG_INF = -POS_INF

    def __init__(self, n: int, iterable) -> None:
        self.n = n
        self.log = (n - 1).bit_length()
        self.tree_size = tree_size = 1 << self.log
        size = 2 * tree_size
        self.hi = [self.NEG_INF] * size
        self.lo = [self.POS_INF] * size
        self.hi2 = [self.NEG_INF] * size
        self.lo2 = [self.POS_INF] * size
        self.nhi = [1] * size
        self.nlo = [1] * size
        self.sum = [0] * size
        self.added = [0] * size
        self.updated = [self.POS_INF] * size
        self.lt = [0] * tree_size
        self.rt = [0] * tree_size
        self.lt.extend(range(tree_size))
        self.rt.extend(range(1, tree_size + 1))

        for i in range(tree_size - 1, 0, -1):
            self.lt[i] = self.lt[i << 1]
            self.rt[i] = self.rt[(i << 1) + 1]

        for i, a in enumerate(iterable, tree_size):
            self.hi[i] = a
            self.lo[i] = a
            self.sum[i] = a
        for i in range(self.tree_size - 1, 0, -1):
            self._merge(i)

    def _merge(self, k: int) -> None:
        left, right = 2 * k, 2 * k + 1
        self.sum[k] = self.sum[left] + self.sum[right]
        hi, lo = self.hi, self.lo
        hi2, lo2 = self.hi2, self.lo2
        # Merge maximum related information.
        if hi[left] < hi[right]:
            hi[k], self.nhi[k] = hi[right], self.nhi[right]
            hi2[k] = max(hi[left], hi2[right])
        elif hi[left] > hi[right]:
            hi[k], self.nhi[k] = hi[left], self.nhi[left]
            hi2[k] = max(hi2[left], hi[right])
        else:
            hi[k] = hi[left]
            self.nhi[k] = self.nhi[left] + self.nhi[right]
            hi2[k] = max(hi2[left], hi2[right])
        # Merge minimum related information.
        if lo[left] > lo[right]:
            lo[k], self.nlo[k] = lo[right], self.nlo[right]
            lo2[k] = min(lo[left], lo2[right])
        elif lo[left] < lo[right]:
            lo[k], self.nlo[k] = lo[left], self.nlo[left]
            lo2[k] = min(lo2[left], lo[right])
        else:
            lo[k] = lo[left]
            self.nlo[k] = self.nlo[left] + self.nlo[right]
            lo2[k] = min(lo2[left], lo2[right])

    def _propagate(self, k: int):
        if self.tree_size <= k:
            return
        left, right = 2 * k, 2 * k + 1
        # Propagate the information from parent to children.
        if self.updated[k] != self.POS_INF:
            self._apply_update(left, self.updated[k])
            self._apply_update(right, self.updated[k])
            self.updated[k] = self.POS_INF
            return
        if self.added[k]:
            self._apply_add(left, self.added[k])
            self._apply_add(right, self.added[k])
            self.added[k] = 0
        # Propagate max and min information to children.
        hi, lo = self.hi, self.lo
        hi2, lo2 = self.hi2, self.lo2
        if hi[k] < hi[left]:
            self._apply_chmax(left, hi[k])
        if lo[left] < lo[k]:
            self._apply_chmin(left, lo[k])
        if hi[k] < hi[right]:
            self._apply_chmax(right, hi[k])
        if lo[right] < lo[k]:
            self._apply_chmin(right, lo[k])

    def _apply_update(self, k: int, x):
        """Update k to x."""
        self.hi[k], self.lo[k] = x, x
        self.hi2[k], self.lo2[k] = self.NEG_INF, self.POS_INF
        diff = self.rt[k] - self.lt[k]
        self.nhi[k], self.nlo[k] = diff, diff
        self.sum[k] = x * diff
        self.added[k] = 0
        self.updated[k] = x

    def _apply_add(self, k: int, x):
        """Add x to k."""
        self.hi[k] += x
        if self.hi2[k] != self.NEG_INF:
            self.hi2[k] += x
        self.lo[k] += x
        if self.lo2[k] != self.POS_INF:
            self.lo2[k] += x
        self.sum[k] += x * (self.rt[k] - self.lt[k])
        if self.updated[k] != self.POS_INF:
            self.updated[k] += x
        else:
            self.added[k] += x

    def _apply_chmax(self, k: int, x):
        """Update k to max(x, A[k])."""
        self.sum[k] += (x - self.hi[k]) * self.nhi[k]
        if self.hi[k] == self.lo[k]:
            self.hi[k], self.lo[k] = x, x
        elif self.hi[k] == self.lo2[k]:
            self.hi[k], self.lo2[k] = x, x
        else:
            self.hi[k] = x
        if self.updated[k] != self.POS_INF and x < self.updated[k]:
            self.updated[k] = x

    def _apply_chmin(self, k: int, x):
        """Update k to min(x, A[k])."""
        self.sum[k] += (x - self.lo[k]) * self.nlo[k]
        if self.lo[k] == self.hi[k]:
            self.lo[k], self.hi[k] = x, x
        elif self.lo[k] == self.hi2[k]:
            self.lo[k], self.hi2[k] = x, x
        else:
            self.lo[k] = x
        if self.updated[k] != self.POS_INF and self.updated[k] < x:
            self.updated[k] = x

    def _range_operation(self, l: int, r: int, cmp1, cmp2, apply_func) -> None:
        """Generic method for range operations."""
        stack, order = [1], []
        while stack:
            k = stack.pop()
            if r <= self.lt[k] or self.rt[k] <= l or cmp1(k):
                continue
            if l <= self.lt[k] and self.rt[k] <= r and cmp2(k):
                apply_func(k)
                continue
            order.append(k)
            self._propagate(k)
            stack.extend([2 * k + 1, 2 * k])
        for v in reversed(order):
            self._merge(v)

    def range_chmax(self, l: int, r: int, x: int) -> None:
        """Update in [l, r) to max(x, A[i])."""
        cmp1 = lambda k: x <= self.lo[k]
        cmp2 = lambda k: x < self.lo2[k]
        f = lambda k: self._apply_chmin(k, x)
        self._range_operation(l, r, cmp1, cmp2, f)

    def range_chmin(self, l: int, r: int, x: int) -> None:
        """Update in [l, r) to min(x, A[i])."""
        cmp1 = lambda k: self.hi[k] <= x
        cmp2 = lambda k: self.hi2[k] < x
        f = lambda k: self._apply_chmax(k, x)
        self._range_operation(l, r, cmp1, cmp2, f)

    def range_add(self, l: int, r: int, x: int) -> None:
        """Add x in [l, r)."""
        cmp1 = lambda _: False
        cmp2 = lambda _: True
        f = lambda k: self._apply_add(k, x)
        self._range_operation(l, r, cmp1, cmp2, f)

    def range_update(self, l: int, r: int, x: int) -> None:
        """Update in [l, r) to x."""
        cmp1 = lambda _: False
        cmp2 = lambda _: True
        f = lambda k: self._apply_update(k, x)
        self._range_operation(l, r, cmp1, cmp2, f)

    def _range_query(self, l: int, r: int, initial_value, compare_func):
        """Generic method for range queries."""
        stack, res = [1], initial_value
        while stack:
            k = stack.pop()
            if r <= self.lt[k] or self.rt[k] <= l:
                continue
            if l <= self.lt[k] and self.rt[k] <= r:
                res = compare_func(res, k)
                continue
            self._propagate(k)
            stack.extend([2 * k + 1, 2 * k])
        return res

    def get_max(self, l: int, r: int):
        """Get max [l, r)."""
        initial_value = self.NEG_INF
        compare_func = lambda v, k: max(v, self.hi[k])
        return self._range_query(l, r, initial_value, compare_func)

    def get_min(self, l: int, r: int):
        """Get min [l, r)."""
        initial_value = self.POS_INF
        compare_func = lambda v, k: min(v, self.lo[k])
        return self._range_query(l, r, initial_value, compare_func)

    def get_sum(self, l: int, r: int):
        """Get range sum [l, r)."""
        initial_value = 0
        compare_func = lambda v, k: v + self.sum[k]
        return self._range_query(l, r, initial_value, compare_func)

    def __getitem__(self, i):
        if i < -self.n or self.n <= i:
            raise IndexError(f"index out of range: {i}")
        if i < 0:
            i += self.n
        return self.get_sum(i, i + 1)

    def __setitem__(self, i, val):
        if i < -self.n or self.n <= i:
            raise IndexError(f"index out of range: {i}")
        if i < 0:
            i += self.n
        self.range_update(i, i + 1, val)

    def __iter__(self):
        yield from (self.get_sum(i, i + 1) for i in range(self.n))

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({list(self)})"


pINF = 10**18
nINF = -10**18

class SegmentTreeBeats():
    """
    // Segment Tree Beats
    // 初期化
    // seg = SegmentTreeBeats(N)
    // seg.build(A)

    // range_chmin  - l<=i<r について、 A_i の値を min(A_i, x) に更新
    // range_chmax  - l<=i<r について、 A_i の値を max(A_i, x) に更新
    // range_add    - l<=i<r について、 A_i の値に x を加える
    // range_update - l<=i<r について、 A_i の値を x に更新
    // get_max      - l<=i<r の中の A_i の最大値を求める
    // get_min      - l<=i<r の中の A_i の最小値を求める
    // get_sum      - l<=i<r の A_i の和を求める
    """
    def __init__(self, n):
        self.n = n
        self.log = (n - 1).bit_length()
        self.size = 1 << self.log
        self.fmax = [nINF] * (2 * self.size)
        self.fmin = [pINF] * (2 * self.size)
        self.smax = [nINF] * (2 * self.size)
        self.smin = [pINF] * (2 * self.size)
        self.maxc = [0] * (2 * self.size)
        self.minc = [0] * (2 * self.size)
        self.sum = [0] * (2 * self.size)
        self.add = [0] * (2 * self.size)
        self.upd = [pINF] * (2 * self.size)
        self.up = []
        self.down = []
        self.lt = [0] * (2 * self.size)
        self.rt = [0] * (2 * self.size)
        for i in range(self.size):
            self.lt[self.size + i] = i
            self.rt[self.size + i] = i + 1
        for i in range(self.size)[::-1]:
            self.lt[i] = self.lt[i << 1]
            self.rt[i] = self.rt[(i << 1) + 1]

    def build(self, arr):
        for i, a in enumerate(arr):
            self.fmax[self.size + i] = a
            self.fmin[self.size + i] = a
            self.maxc[self.size + i] = 1
            self.minc[self.size + i] = 1
            self.sum[self.size + i] = a
        for i in range(1, self.size)[::-1]: self.merge(i)

    def merge(self, k):
        self.sum[k] = self.sum[2 * k] + self.sum[2 * k + 1]
        if self.fmax[2 * k] < self.fmax[2 * k + 1]:
            self.fmax[k] = self.fmax[2 * k + 1]
            self.maxc[k] = self.maxc[2 * k + 1]
            self.smax[k] = max(self.fmax[2 * k], self.smax[2 * k + 1])
        elif self.fmax[2 * k] > self.fmax[2 * k + 1]:
            self.fmax[k] = self.fmax[2 * k]
            self.maxc[k] = self.maxc[2 * k]
            self.smax[k] = max(self.smax[2 * k], self.fmax[2 * k + 1])
        else:
            self.fmax[k] = self.fmax[2 * k]
            self.maxc[k] = self.maxc[2 * k] + self.maxc[2 * k + 1]
            self.smax[k] = max(self.smax[2 * k], self.smax[2 * k + 1])
        if self.fmin[2 * k] > self.fmin[2 * k + 1]:
            self.fmin[k] = self.fmin[2 * k + 1]
            self.minc[k] = self.minc[2 * k + 1]
            self.smin[k] = min(self.fmin[2 * k], self.smin[2 * k + 1])
        elif self.fmin[2 * k] < self.fmin[2 * k + 1]:
            self.fmin[k] = self.fmin[2 * k]
            self.minc[k] = self.minc[2 * k]
            self.smin[k] = min(self.smin[2 * k], self.fmin[2 * k + 1])
        else:
            self.fmin[k] = self.fmin[2 * k]
            self.minc[k] = self.minc[2 * k] + self.minc[2 * k + 1]
            self.smin[k] = min(self.smin[2 * k], self.smin[2 * k + 1])

    def propagate(self, k):
        if self.size <= k: return #?
        if self.upd[k] != pINF:
            self.update_(2 * k, self.upd[k])
            self.update_(2 * k + 1, self.upd[k])
            self.upd[k] = pINF
            return
        if self.add[k]:
            self.add_(2 * k, self.add[k])
            self.add_(2 * k + 1, self.add[k])
            self.add[k] = 0
        if self.fmax[k] < self.fmax[2 * k]:
            self.chmax_(2 * k, self.fmax[k])
        if self.fmin[2 * k] < self.fmin[k]:
            self.chmin_(2 * k, self.fmin[k])
        if self.fmax[k] < self.fmax[2 * k + 1]:
            self.chmax_(2 * k + 1, self.fmax[k])
        if self.fmin[2 * k + 1] < self.fmin[k]:
            self.chmin_(2 * k + 1, self.fmin[k])

    def up_merge(self):
        while self.up:
            self.merge(self.up.pop())

    def down_propagate(self, k):
        self.propagate(k)
        self.down.append(2 * k)
        self.down.append(2 * k + 1)

    def update_(self, k, x):
        self.fmax[k] = x
        self.smax[k] = nINF
        self.fmin[k] = x
        self.smin[k] = pINF
        self.maxc[k] = self.rt[k] - self.lt[k]
        self.minc[k] = self.rt[k] - self.lt[k]
        self.sum[k] = x * (self.rt[k] - self.lt[k])
        self.add[k] = 0
        self.upd[k] = x

    def add_(self, k, x):
        self.fmax[k] += x
        if self.smax[k] != nINF: self.smax[k] += x
        self.fmin[k] += x
        if self.smin[k] != pINF: self.smin[k] += x
        self.sum[k] += x * (self.rt[k] - self.lt[k])
        if self.upd[k] != pINF:
            self.upd[k] += x
        else:
            self.add[k] += x

    def chmax_(self, k, x):
        self.sum[k] += (x - self.fmax[k]) * self.maxc[k]
        if self.fmax[k] == self.fmin[k]:
            self.fmax[k] = x
            self.fmin[k] = x
        elif self.fmax[k] == self.smin[k]:
            self.fmax[k] = x
            self.smin[k] = x
        else:
            self.fmax[k] = x
        if self.upd[k] != pINF and x < self.upd[k]:
            self.upd[k] = x

    def chmin_(self, k, x):
        self.sum[k] += (x - self.fmin[k]) * self.minc[k]
        if self.fmin[k] == self.fmax[k]:
            self.fmin[k] = x
            self.fmax[k] = x
        elif self.fmin[k] == self.smax[k]:
            self.fmin[k] = x
            self.smax[k] = x
        else:
            self.fmin[k] = x
        if self.upd[k] != pINF and self.upd[k] < x:
            self.upd[k] = x

    def range_chmax(self, a, b, x):
        self.down.append(1)
        while self.down:
            k = self.down.pop()
            if b <= self.lt[k] or self.rt[k] <= a or x <= self.fmin[k]: continue
            if a <= self.lt[k] and self.rt[k] <= b and x < self.smin[k]:
                self.chmin_(k, x)
                continue
            self.down_propagate(k)
            self.up.append(k)
        self.up_merge()

    def range_chmin(self, a, b, x):
        self.down.append(1)
        while self.down:
            k = self.down.pop()
            if b <= self.lt[k] or self.rt[k] <= a or self.fmax[k] <= x: continue
            if a <= self.lt[k] and self.rt[k] <= b and self.smax[k] < x:
                self.chmax_(k, x)
                continue
            self.down_propagate(k)
            self.up.append(k)
        self.up_merge()

    def range_add(self, a, b, x):
        self.down.append(1)
        while self.down:
            k = self.down.pop()
            if b <= self.lt[k] or self.rt[k] <= a: continue
            if a <= self.lt[k] and self.rt[k] <= b:
                self.add_(k, x)
                continue
            self.down_propagate(k)
            self.up.append(k)
        self.up_merge()

    def range_update(self, a, b, x):
        self.down.append(1)
        while self.down:
            k = self.down.pop()
            if b <= self.lt[k] or self.rt[k] <= a: continue
            if a <= self.lt[k] and self.rt[k] <= b:
                self.update_(k, x)
                continue
            self.down_propagate(k)
            self.up.append(k)
        self.up_merge()

    def get_max(self, a, b):
        self.down.append(1)
        v = nINF
        while self.down:
            k = self.down.pop()
            if b <= self.lt[k] or self.rt[k] <= a: continue
            if a <= self.lt[k] and self.rt[k] <= b:
                v = max(v, self.fmax[k])
                continue
            self.down_propagate(k)
        return v

    def get_min(self, a, b):
        self.down.append(1)
        v = pINF
        while self.down:
            k = self.down.pop()
            if b <= self.lt[k] or self.rt[k] <= a: continue
            if a <= self.lt[k] and self.rt[k] <= b:
                v = min(v, self.fmin[k])
                continue
            self.down_propagate(k)
        return v

    def get_sum(self, a, b):
        self.down.append(1)
        v = 0
        while self.down:
            k = self.down.pop()
            if b <= self.lt[k] or self.rt[k] <= a: continue
            if a <= self.lt[k] and self.rt[k] <= b:
                v += self.sum[k]
                continue
            self.down_propagate(k)
        return v


def main():
    # TLEしたのでC++に
    # https://judge.yosupo.jp/submission/204887 をペタリ
    N = NI()
    A = NLI()
    Q = NI()
    LRK = EI(Q)
    stb = SegmentTreeBeats(N)
    stb.build(A)
    for l, r, k in LRK:
        l -= 1
        s = stb.get_sum(l, r)
        stb.range_add(l, r, -k)
        stb.range_chmax(l, r, 0)
        ss = stb.get_sum(l, r)
        print(s - ss)


if __name__ == "__main__":
    main()
