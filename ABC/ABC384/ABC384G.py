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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped = {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
    return zipped


def main():
    N = NI()
    A = NLI()
    B = NLI()
    Q = NI()
    sz = (N // math.isqrt(Q)) + 1
    # sz = 1000
    XYI = [[x, y, i] for i, (x, y) in enumerate(EI(Q))]
    XYI.sort(key=lambda xyi: (xyi[1]//sz, xyi[0]*(-1)**((xyi[1]//sz)%2)))

    Z = compress(A+B)
    ZN = len(Z)
    numA = BIT(ZN)
    numB = BIT(ZN)
    sumA = BIT(ZN)
    sumB = BIT(ZN)

    Acomp = [Z[a] for a in A]
    Bcomp = [Z[b] for b in B]

    ans = [0] * Q
    nx, ny = 0, 0
    now = 0
    total_a = 0
    total_b = 0
    for x, y, i in XYI:
        while nx < x:
            v = A[nx]
            z = Acomp[nx]
            lower = sumB.sum0(z)
            upper = total_b - lower
            lower_num = numB.sum0(z)
            now += upper - (ny - lower_num) * v
            now += lower_num * v - lower
            numA.add(z, 1)
            sumA.add(z, v)
            total_a += v
            nx += 1
        while nx > x:
            v = A[nx-1]
            z = Acomp[nx-1]
            lower = sumB.sum0(z)
            upper = total_b - lower
            lower_num = numB.sum0(z)
            now -= upper - (ny - lower_num) * v
            now -= lower_num * v - lower
            numA.add(z, -1)
            sumA.add(z, -v)
            total_a -= v
            nx -= 1
        while ny < y:
            v = B[ny]
            z = Bcomp[ny]
            lower = sumA.sum0(z)
            upper = total_a - lower
            lower_num = numA.sum0(z)
            now += upper - (nx - lower_num) * v
            now += lower_num * v - lower
            numB.add(z, 1)
            sumB.add(z, v)
            total_b += v
            ny += 1
        while ny > y:
            v = B[ny-1]
            z = Bcomp[ny-1]
            lower = sumA.sum0(z)
            upper = total_a - lower
            lower_num = numA.sum0(z)
            now -= upper - (nx - lower_num) * v
            now -= lower_num * v - lower
            numB.add(z, -1)
            sumB.add(z, -v)
            total_b -= v
            ny -= 1
        ans[i] = now

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
