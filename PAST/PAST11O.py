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


class Point:
    def __init__(self, x, y):
        g = math.gcd(x, y)
        self.x = x // g
        self.y = y // g
        if y >= 0 and x > 0:
            self.quad = 1
        elif x <= 0 and y > 0:
            self.quad = 2
        elif y <= 0 and x < 0:
            self.quad = 3
        elif x >= 0 and y < 0:
            self.quad = 4
        else:
            self.quad = 0

    def counter(self):
        return Point(-self.x, -self.y)

    def __hash__(self):
        return self.x * 10**6 + self.y

    def __lt__(self, other):
        if self.quad != other.quad:
            return self.quad < other.quad
        else:
            cross = self.x * other.y - self.y * other.x
            return cross > 0

    def __eq__(self, other):
        return self.quad == other.quad and self.x * other.y - self.y * other.x == 0

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


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
            self.data[p - 1] %= MOD99
            p += p & -p

    def get(self, p):
        return self.sum(p, p + 1)

    def sum(self, l, r):
        assert (0 <= l and l <= r and r <= self.n), "0<=l<=r<=n,l={0},r={1},n={2}".format(l, r, self.n)
        return (self.sum0(r) - self.sum0(l)) % MOD99

    def sum0(self, r):
        s = 0
        while (r > 0):
            s += self.data[r - 1]
            s %= MOD99
            r -= r & -r
        return s

    def debug(self):
        res = [self.get(p) for p in range(self.n)]
        return res


def main():
    Q = NI()
    querys = [SLI() for _ in range(Q)]
    XY = []
    for q, x, y in querys:
        x, y = int(x), int(y)
        XY.append(Point(x, y))
        XY.append(Point(x, y).counter())

    Z, UZ = compress(XY)
    bitx = BIT(len(Z))
    bity = BIT(len(Z))
    ans = 0

    for q, x, y in querys:
        x, y = int(x), int(y)
        p = Point(x, y)
        c = p.counter()
        zp, zc = Z[p], Z[c]

        if q == "+":
            if zp < zc:
                ys = bity.sum(zp, zc)
                xs = bitx.sum(zp, zc)
                ans += ys * x - xs * y
                ans -= (bity.sum0(bity.n) - ys) * x - (bitx.sum0(bitx.n) - xs) * y
            else:
                ys = bity.sum(zc, zp)
                xs = bitx.sum(zc, zp)
                ans -= ys * x - xs * y
                ans += (bity.sum0(bity.n) - ys) * x - (bitx.sum0(bitx.n) - xs) * y

            bitx.add(zp, x)
            bity.add(zp, y)

        else:
            if zp < zc:
                ys = bity.sum(zp, zc)
                xs = bitx.sum(zp, zc)
                ans -= ys * x - xs * y
                ans += (bity.sum0(bity.n) - ys) * x - (bitx.sum0(bitx.n) - xs) * y
            else:
                ys = bity.sum(zc, zp)
                xs = bitx.sum(zc, zp)
                ans += ys * x - xs * y
                ans -= (bity.sum0(bity.n) - ys) * x - (bitx.sum0(bitx.n) - xs) * y

            bitx.add(zp, -x)
            bity.add(zp, -y)

        ans %= MOD99
        print(ans)



if __name__ == "__main__":
    main()
