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
    N, K = NMI()
    P = NLI()

    if K == 0:
        print(*P)
        exit()

    # 回転無し
    INF = 10**15
    tree = segtree(P, min, INF)

    p2i = [0] * (N+1)
    for i, p in enumerate(P):
        p2i[p] = i

    l = 0
    r = min(K+1, N)
    ans1 = []
    while l < N:
        m = tree.prod(l, r)
        mi = p2i[m]

        k = mi - len(ans1)
        if k > K:
            break

        ans1.append(m)
        l = mi + 1
        r = min(l + K-k + 1, N)

    # 回転あり
    m = min(P[-K:])
    X = P.index(m)

    P = P[X:] + P[:X]

    INF = 10**15
    tree = segtree(P, min, INF)

    p2i = [0] * (N+1)
    for i, p in enumerate(P):
        p2i[p] = i

    l = 0
    r = min(K+1, N)
    k = N - X
    ans2 = []
    while l < N:
        m = tree.prod(l, r)
        # print(l, r, m, k)
        mi = p2i[m]
        if mi >= N - X:
            k += mi - max(l, N-X)

            ans2.append(m)
            l = mi + 1
            r = min(l + K - k + 1, N)

        else:
            ans2.append(m)
            l = mi + 1
            r = min(K+1, N)

    ans = min(ans1, ans2)
    print(*ans)


def _main():
    N, K = NMI()
    P = NLI()
    if K == 0:
        print(*P)
        exit()

    m = min(P[-K:])
    mi = P.index(m)

    P = P[mi:] + P[:mi]

    p2i = [0] * (N+1)
    for i, p in enumerate(P):
        p2i[p] = i

    k = N - mi
    idx = 0
    ans = []

    for p in range(1, N+1):
        # print(p, p2i[p])
        pi = p2i[p]
        if pi < idx:
            continue

        if pi < N - mi:
            ans.append(p)
            idx = pi + 1
            # print(f"{p} within f, idx={idx}")
        elif pi <= K:
            k += pi - idx - 1
            if k > K:
                break
            ans.append(p)
            idx = pi + 1
            # print(f"{p} within K, idx={idx}")

    print(*ans)


if __name__ == "__main__":
    main()