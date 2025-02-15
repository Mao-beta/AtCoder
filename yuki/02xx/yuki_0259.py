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
    N, Q = NMI()
    # N-1, N-2, ..., 1, 0, 0, 1, ..., N-1
    # 魚はこの中を全部右に動き、端で消えて左から出てくるとする
    # Rの魚は右側、Lの魚は左側に入るが、そこからt巻き戻した位置に入れる
    # Cは2箇所作ったうえでtずらす
    bit = BIT(2*N)
    for _ in range(Q):
        x, t, y, z = SMI()
        t = int(t)
        y, z = int(y), int(z)
        if x == "L":
            p = (N-1-y-t) % (2*N)
            bit.add(p, z)
        elif x == "R":
            p = (y+N-t) % (2*N)
            bit.add(p, z)
        else:
            ans = 0
            ry, rz = N+y-t, N+z-t
            ly, lz = N-z-t, N-y-t
            # print(t, ly, lz, ry, rz)

            if ry // (2*N) == rz // (2*N):
                ans += bit.sum(ry % (2*N), rz % (2*N))
            else:
                ans += bit.sum(0, rz % (2 * N))
                ans += bit.sum(ry % (2 * N), 2*N)

            if ly // (2*N) == lz // (2*N):
                ans += bit.sum(ly % (2*N), lz % (2*N))
            else:
                ans += bit.sum(0, lz % (2 * N))
                ans += bit.sum(ly % (2 * N), 2*N)

            print(ans)

        # print(x, y, z, bit.debug())


if __name__ == "__main__":
    main()
