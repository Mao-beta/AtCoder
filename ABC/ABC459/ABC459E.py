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

from collections import deque


def topological_sort(graph):
    """
    BFSによるトポロジカルソート O(V+E)
    :param graph: 隣接リスト
    :return: 長さnならトポソ可能、そうでなければサイクルあり
    """
    n = len(graph)
    dims = [0] * n
    for i, adj in enumerate(graph):
        for goto in adj:
            dims[goto] += 1

    que = deque()
    for i, d in enumerate(dims):
        if d == 0:
            que.append(i)

    res = []
    while que:
        now = que.popleft()
        res.append(now)

        for goto in graph[now]:
            dims[goto] -= 1
            if dims[goto] == 0:
                que.append(goto)

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


class Comb:
    """nCrのnもrも10**7くらいまで"""

    def __init__(self, n, mod):
        self.mod = mod
        self.fac = [1] * (n + 1)
        self.inv = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fac[i] = self.fac[i - 1] * i % self.mod
        self.inv[n] = pow(self.fac[n], self.mod - 2, self.mod)
        for i in range(n - 1, 0, -1):
            self.inv[i] = self.inv[i + 1] * (i + 1) % self.mod

    def C(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self.fac[n] * self.inv[r] % self.mod * self.inv[n - r] % self.mod

    def P(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self.fac[n] * self.inv[n - r] % self.mod

    def H(self, n, r):
        """
        n個のものから重複を許してr個取り出す
        """
        if n == r == 0:
            return 1
        return self.C(n + r - 1, r)

    def multi(self, L):
        res = self.fac[sum(L)]
        for l in L:
            res = res * self.inv[l] % self.mod
        return res


class HugeComb:
    """nCrのnが10**9くらいあるが、rが10**5くらい"""
    def __init__(self, r_max, mod=10**9+7):
        assert r_max >= 0
        self.r_max = r_max
        self.inv = [1] * (r_max+1)
        self.mod = mod

        for i in range(1, r_max+1):
            a = self.inv[i-1] * pow(i, mod-2, mod) % mod
            self.inv[i] = a

    def P(self, n, r):
        assert r >= 0
        assert n >= r
        res = 1
        for i in range(r):
            res = res * (n-i) % self.mod
        return res

    def C(self, n, r):
        assert r <= self.r_max
        return self.P(n, r) * self.inv[r] % self.mod

    def H(self, n, r):
        return self.C(n+r-1, r-1)


def main():
    N = NI()
    P = NLI()
    E = [[i, P[i-2]] for i in range(2, N+1)]

    com = HugeComb(10**6, MOD99)

    G = adjlist(N, E, directed=True)
    C = NLI()
    D = NLI()
    topo = topological_sort(G)

    rem = [0] * N
    ans = 1
    for u in topo:
        p, c, d, r = P[u-1]-1, C[u], D[u], rem[u]
        if c+r < d:
            ans = 0
            break
        ans = ans * com.C(c+r, d) % MOD99
        rem[p] += c+r-d
    print(ans)


if __name__ == "__main__":
    main()
