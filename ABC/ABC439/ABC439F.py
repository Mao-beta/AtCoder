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
    N = NI()
    P = NLI()
    if N <= 2:
        print(0)
        return

    if N == 3:
        if P[1] == 3:
            print(1)
            return
        else:
            print(0)
            return

    # L2: 左からi番目が部分列の左から2個目であるときの数
    # R2: 左からi番目が部分列の右から2個目であるときの数
    ans = 0
    bitL = BIT(N+1)
    bitR = BIT(N+1)
    bit = BIT(N+1) # 部分列の長さが3のとき用
    L2 = [0] * N
    R2 = [0] * N
    for i in range(N):
        p = P[i]
        L2[i] = bitL.sum(0, p)
        bitL.add(p, 1)
        bit.add(p, L2[i])
    for i in range(N-1, -1, -1):
        p = P[i]
        R2[i] = bitR.sum(0, p)
        bitR.add(p, 1)
        bit.add(p, -L2[i])
        ans += bit.sum(p+1, N+1)
    cum = 0
    for i in range(N-3, 0, -1):
        cum += R2[i+1]
        # print(R2[i+1], L2[i], cum)
        ans += L2[i] * cum
        ans %= MOD99
        cum *= 2
        cum %= MOD99
    # print(L2, R2)
    print(ans)


if __name__ == "__main__":
    main()
