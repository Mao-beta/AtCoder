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

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

    def get_roots(self):
        return self.roots

    def group_count(self):
        return len(self.roots)


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(S):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N, K = NMI()
    XY = [NLI() for _ in range(N)]

    if K == 1:
        print("Infinity")
        exit()

    edges = []
    for i in range(N):
        for j in range(i+1, N):
            edges.append(i*N + j)

    Z, UZ = compress(edges)
    # print(Z)
    uf = UnionFind(len(Z))

    for i in range(N):
        ax, ay = XY[i]
        for j in range(i+1, N):
            bx, by = XY[j]
            for k in range(j+1, N):
                cx, cy = XY[k]
                e1 = Z[i*N+j]
                e2 = Z[j*N+k]
                e3 = Z[i*N+k]

                abx = ax - bx
                aby = ay - by
                bcx = bx - cx
                bcy = by - cy

                if abx * bcy == aby * bcx:
                    # print(i, j, k)
                    if not uf.is_same(e1, e2):
                        uf.unite(e1, e2)
                    if not uf.is_same(e1, e3):
                        uf.unite(e1, e3)

    ans = 0
    for r in uf.roots:
        if uf.size(r) >= K * (K-1) // 2:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
