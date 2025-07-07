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
    N, M = NMI()
    AB = EI(M)
    Q = NI()
    CD = EI(Q)
    bit = BIT(N*4)
    AB = [[x-1, y-1] for x, y in AB]
    CD = [[x-1, y-1] for x, y in CD]
    for a, b in AB:
        bit.add(a, 1)
        bit.add(b, -1)
    C2DI = [[] for _ in range(2*N)]
    for i, (c, d) in enumerate(CD):
        C2DI[c].append([d, i])
    A2BI = [[] for _ in range(2*N)]
    for i, (a, b) in enumerate(AB):
        A2BI[a].append([b, i])
    ans = [0] * Q
    for x in range(2*N):
        for b, i in A2BI[x]:
            bit.add(x, -1)
            bit.add(b, 2)
            bit.add(x+2*N, -1)
        for d, i in C2DI[x]:
            # print(f"query{i} {x=} {d=} {bit.sum(x, d+1)}")
            ans[i] = bit.sum(x, d+1)
        # print(x, bit.debug())
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
