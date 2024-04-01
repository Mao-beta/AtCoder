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
    X = NLI()
    X = [x-1 for x in X]
    bit = BIT(Q+1)
    S = set()
    total = 0
    Y = [[0] for _ in range(N)]

    for q, x in enumerate(X):
        Y[x].append(q)
        if x in S:
            S.discard(x)
            total -= 1
        else:
            S.add(x)
            total += 1
        bit.add(q, total)
    
    # print(bit.debug())
    # print(*Y, sep="\n")

    s = bit.sum(0, Q+1)
    ans = [s] * N
    for x, y in enumerate(Y):
        y.append(Q)
        for i in range(len(y)//2):
            l = y[i*2]
            r = y[i*2+1]
            ans[x] -= bit.sum(l, r)
    print(*ans)


if __name__ == "__main__":
    main()
