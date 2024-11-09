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


LINF = int(4e18)
INF = int(1e9) + 10

class S:
    def __init__(self, min_val, max_val, sum_val, l, r):
        self.min = min_val
        self.max = max_val
        self.sum = sum_val
        self.l = l
        self.r = r

    def __repr__(self):
        return f"{self.sum=}"

class F:
    def __init__(self, a=LINF, b=LINF):
        self.a = a
        self.b = b

def op(s1, s2):
    return S(min(s1.min, s2.min), max(s1.max, s2.max), s1.sum + s2.sum, min(s1.l, s2.l), max(s1.r, s2.r))

def e():
    return S(LINF, -LINF, 0, INF, -INF)

def mapping(f, s):
    if f.a == LINF:
        return s
    if f.a >= 0:
        new_min = f.a * s.l + f.b
        new_max = f.a * (s.r - 1) + f.b
        new_sum = (f.a * (s.l + s.r - 1) + f.b * 2) * (s.r - s.l) // 2
        return S(new_min, new_max, new_sum, s.l, s.r)
    else:
        new_min = f.a * (s.r - 1) + f.b
        new_max = f.a * s.l + f.b
        new_sum = (f.a * (s.l + s.r - 1) + f.b * 2) * (s.r - s.l) // 2
        return S(new_min, new_max, new_sum, s.l, s.r)

def composition(f1, f2):
    return f2 if f1.a == LINF else f1

def id():
    return F(LINF, LINF)

class LazySegmentTreeArithmetic:
    def __init__(self, n_or_v):
        if isinstance(n_or_v, int):
            self.n = n_or_v
            self.tree = [e()] * (2 * self.n)
            for i in range(self.n):
                self.tree[self.n + i] = S(0, 0, 0, i, i + 1)
        elif isinstance(n_or_v, list):
            self.n = len(n_or_v)
            self.tree = [e()] * (2 * self.n)
            for i, val in enumerate(n_or_v):
                self.tree[self.n + i] = S(val, val, val, i, i + 1)
        else:
            raise ValueError("Input should be either an integer or a list")
        self.lazy = [id()] * self.n

    def apply(self, l, r, f):
        self._apply(l, r, F(f.a, f.b - f.a * self.get(l).l))

    def get(self, p):
        # Utility to get the value at position `p` (used for lazy propagation)
        p += self.n
        res = self.tree[p]
        while p > 1:
            p //= 2
            res = op(self.tree[p], res)
        return res

    def _apply(self, l, r, f):
        # Apply function F to range [l, r)
        l += self.n
        r += self.n
        while l < r:
            if l % 2 == 1:
                self.tree[l] = mapping(f, self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                self.tree[r] = mapping(f, self.tree[r])
            l //= 2
            r //= 2


def main():
    N = NI()
    X = NLI()
    Q = NI()
    TG = EI(Q)
    seg = LazySegmentTreeArithmetic(X)
    seg.apply(0, 3, F(1, 0))
    print([seg.get(i) for i in range(N)])



if __name__ == "__main__":
    main()
