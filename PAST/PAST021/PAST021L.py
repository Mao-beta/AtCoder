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


from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n
        self.roots = set(range(n))
        self.group_num = n

    def find(self, x):
        # 根ならその番号を返す
        if self.par[x] < 0:
            return x
        else:
            # 親の親は親
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def is_same(self, x, y):
        # 根が同じならTrue
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return

        # 木のサイズを比較し、小さいほうから大きいほうへつなぐ
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.group_num -= 1
        self.roots.discard(y)
        assert self.group_num == len(self.roots)

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

    def get_roots(self):
        return self.roots

    def group_count(self):
        return len(self.roots)


def MST(N, edges):
    """
    要UnionFind
    N頂点の最小全域木の長さ
    edges = [[u, v, cost], ....] (0-index)
    """
    uf = UnionFind(N)
    edges.sort(key=lambda x: x[-1])
    res = 0
    for a, b, c in edges:
        if uf.is_same(a, b):
            continue
        else:
            res += c
            uf.unite(a, b)
        if uf.group_num == 1:
            break
    return res, uf



def main():
    N = NI()
    XY = EI(N)
    P = NLI()
    edges = []
    for i in range(N):
        for j in range(i+1, N):
            xi, yi = XY[i]
            xj, yj = XY[j]
            d = math.sqrt((xi - xj)**2 + (yi - yj)**2)
            edges.append((i, j, d))
        edges.append((i, N, P[i]))
    print(MST(N+1, edges)[0])


if __name__ == "__main__":
    main()
