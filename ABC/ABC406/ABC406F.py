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


def adjlist(n, edges, directed=False, in_origin=1) -> list[list[int]]:
    if len(edges) == 0:
        return [[] for _ in range(n)]

    weighted = True if len(edges[0]) > 2 else False
    if in_origin == 1:
        if weighted:
            edges = [[x-1, y-1, w] for x, y, w in edges]
        else:
            edges = [[x-1, y-1] for x, y in edges]

    res = [[] for _ in range(n)]

    if weighted:
        for u, v, c in edges:
            res[u].append([v, c])
            if not directed:
                res[v].append([u, c])

    else:
        for u, v in edges:
            res[u].append(v)
            if not directed:
                res[v].append(u)

    return res


def main():
    N = NI()
    UV = EI(N-1)
    E2UV = []
    for i, (u, v) in enumerate(UV):
        E2UV.append([u-1, v-1])
    G = adjlist(N, UV)
    # オイラーツアー
    # visit, discover, finishを求める
    def EulerTour(n, X, i0):
        # https://qiita.com/Kiri8128/items/2b0023bed9af642c751c
        # Xは破壊してXとPができる
        P = [-1] * n
        Q = [~i0, i0]
        ct = -1
        ET = [] # visit
        ET1 = [0] * n # discover
        ET2 = [0] * n # finish
        DE = [0] * n
        de = -1
        while Q:
            i = Q.pop()
            if i < 0:
                # ↓ 戻りも数字を足す場合はこれを使う
                # ct += 1
                # ↓ 戻りもETに入れる場合はこれを使う
                # ET.append(P[~i])
                ET2[~i] = ct
                de -= 1
                continue
            if i >= 0:
                ET.append(i)
                ct += 1
                if ET1[i] == 0: ET1[i] = ct
                de += 1
                DE[i] = de
            for a in X[i][::-1]:
                if a != P[i]:
                    P[a] = i
                    for k in range(len(X[a])):
                        if X[a][k] == i:
                            del X[a][k]
                            break
                    Q.append(~a)
                    Q.append(a)
        return (ET, ET1, ET2)

    visit, discover, finish = EulerTour(N, G, 0)
    BN = len(visit)
    bit = BIT(BN)
    for d in discover:
        bit.add(d, 1)

    total = N
    Q = NI()
    for _ in range(Q):
        q, *X = NMI()
        if q == 1:
            x, w = X
            x -= 1
            bit.add(discover[x], w)
            total += w
        else:
            y = X[0] - 1
            u, v = E2UV[y]
            if discover[u] > discover[v]:
                u, v = v, u
            vsum = bit.sum(discover[v], finish[v])
            print(abs((total - vsum) - vsum))


if __name__ == "__main__":
    main()
