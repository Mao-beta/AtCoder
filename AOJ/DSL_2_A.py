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


class segtree:
    def __init__(self, N, func, e):
        self.N = N
        self.func = func
        self.e = e

        b = len(bin(self.N - 1)[2:])
        self.size = 1 << b

        self.tree = [self.e] * self.size * 2

    def update(self, i, x):
        i += self.size
        l, r = i, i+1
        a = x
        while l > 0:
            self.tree[l] = a
            if l % 2:
                a = self.func(self.tree[l-1], a)
                l -= 1
            if r % 2:
                a = self.func(a, self.tree[r])
                r += 1
            l >>= 1
            r >>= 1

    def find(self, l, r):
        l += self.size
        r += self.size
        al = self.e
        ar = self.e
        while l < r:
            if l % 2:
                al = self.func(al, self.tree[l])
                l += 1
            if r % 2:
                ar = self.func(self.tree[r-1], ar)
                r -= 1
            l >>= 1
            r >>= 1
        a = self.func(al, ar)
        return a


    def get(self, i):
        i += self.size
        return self.tree[i]

    def each(self):
        return self.tree[self.size:]

    def __repr__(self):
        return str(self.each())


def main():
    N, Q = NMI()

    INF = (1 << 31) - 1
    seg = segtree(N, min, INF)

    for _ in range(Q):
        c, x, y = NMI()
        if c == 0:
            seg.update(x, y)
        else:
            y += 1
            print(seg.find(x, y))
        # print(seg)



if __name__ == "__main__":
    main()
