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
    A = NLI()
    C = Counter(A)

    # D[i]: i個持ち越しているときの場合の数
    D = BIT(1)
    D.add(0, 1)

    for a in range(1, max(A)+30):

        # for k, v in D.items():
        #     print(k, v)
        #     # M個ぶん持ち越せる
        #     M = (k + C[a]) // 2
        #     for nk in range(M+1):
        #         D2[nk] += v
        #         D2[nk] %= MOD99

        M = (D.n - 1 + C[a]) // 2
        D2 = BIT(M+1)
        for k in range(M+1):
            x = 0
            if k * 2 <= C[a]:
                x = D.sum(0, D.n)
            else:
                rem = k * 2 - C[a]
                if 0 <= rem <= D.n:
                    x = D.sum(rem, D.n)
            D2.add(k, x % MOD99)

        D = D2

    print(D.sum(0, D.n) % MOD99)


if __name__ == "__main__":
    main()
