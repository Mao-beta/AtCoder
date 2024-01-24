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

    def set(self, p, x):
        b = self.get(p)
        self.add(p, -b)
        self.add(p, x)

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
    H, W, M = NMI()
    XY = EI(M)
    XY = [[x-1, y-1] for x, y in XY]
    H0, W0 = H, W
    H2W = [[] for _ in range(H)]
    for x, y in XY:
        H2W[x].append(y)
        if x == 0:
            W0 = min(W0, y)
        if y == 0:
            H0 = min(H0, x)

    h2rem = [W-W0] * H0
    w2rem = [H-H0] * W0
    bit = BIT(W0)
    bad = 0
    for h in range(H):
        if h < H0:
            for w in H2W[h]:
                if w < W0:
                    w2rem[w] = 0
                    bit.set(w, 1)
                    h2rem[h] = 0
                else:
                    h2rem[h] = min(h2rem[h], w-W0)

            if H2W[h]:
                minw = min(H2W[h])
                if minw < W0:
                    bad += bit.sum(minw, W0)
        else:
            for w in H2W[h]:
                if w < W0:
                    w2rem[w] = min(w2rem[w], h-H0)
    ans = H0 * W0 - bad + sum(h2rem) + sum(w2rem)
    # print(H0, W0, bad, h2rem, w2rem)
    print(ans)


if __name__ == "__main__":
    main()
