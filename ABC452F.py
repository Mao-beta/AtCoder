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


def main():
    N, K = NMI()
    P = NLI()
    P = [x-1 for x in P]
    bitk = BIT(N)
    bitk1 = BIT(N)
    r = 0
    r1 = 0
    k = 0
    k1 = 0
    ans = 0
    for l in range(N):
        while r < N:
            x = P[r]
            add = bitk.sum(x+1, N)
            if k + add <= K:
                r += 1
                k += add
                bitk.add(x, 1)
            else:
                break
        while r1 < N:
            x = P[r1]
            add = bitk1.sum(x+1, N)
            if k1 + add <= K-1:
                r1 += 1
                k1 += add
                bitk1.add(x, 1)
            else:
                break
        r = max(r, l)
        r1 = max(r1, l)
        ans += r - r1
        # print(l, r, r1)
        x = P[l]
        if l < r:
            gap = bitk.sum(0, x)
            k -= gap
            bitk.add(x, -1)
        if l < r1:
            gap = bitk1.sum(0, x)
            k1 -= gap
            bitk1.add(x, -1)
        r = max(r, l)
        r1 = max(r1, l)
        # print(l, r, r1)
    print(ans)


if __name__ == "__main__":
    main()
