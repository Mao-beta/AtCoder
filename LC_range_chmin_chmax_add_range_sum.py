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
    N, Q = NMI()
    A = NLI()
    seg = SegmentTreeBeats(N)
    seg.build(A)
    ans = []
    for _ in range(Q):
        q, *X = NMI()

        if q == 0:
            seg.range_chmin(*X)
        elif q == 1:
            seg.range_chmax(*X)
        elif q == 2:
            seg.range_add(*X)
        else:
            print(seg.get_sum(*X))


    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
