import sys
import math
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


class UnionFind:
    def __init__(self, n):
        #親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n

    def find(self, x):
        #根ならその番号を返す
        if self.par[x] < 0:
            return x
        else:
            #親の親は親
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def is_same(self, x, y):
        #根が同じならTrue
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return

        #木のサイズを比較し、小さいほうから大きいほうへつなぐ
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __repr__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    N, K = NMI()
    A = [NLI() for _ in range(N)]
    is_ok_row = make_grid(N, N, 0)
    is_ok_col = make_grid(N, N, 0)
    cols = [[] for _ in range(N)]
    for row in A:
        for c, a in enumerate(row):
            cols[c].append(a)

    set_row = set()
    set_col = set()
    uf_row = UnionFind(N)
    uf_col = UnionFind(N)

    for i in range(N):
        for j in range(i+1, N):
            row_i = A[i]
            row_j = A[j]
            sum_row = [x+y for x, y in zip(row_i, row_j)]
            if max(sum_row) <= K:
                is_ok_row[i][j] = 1
                is_ok_row[j][i] = 1
                set_row.add(i)
                set_row.add(j)
                uf_row.unite(i, j)

            col_i = cols[i]
            col_j = cols[j]
            sum_col = [x+y for x, y in zip(col_i, col_j)]
            if max(sum_col) <= K:
                is_ok_col[i][j] = 1
                is_ok_col[j][i] = 1
                set_col.add(i)
                set_col.add(j)
                uf_col.unite(i, j)


    row_groups = uf_row.all_group_members()
    col_groups = uf_col.all_group_members()
    ans = 1
    for L in list(row_groups.values()):
        if len(L) == 1: continue
        ans = ans * math.factorial(len(L)) % MOD
    for L in list(col_groups.values()):
        if len(L) == 1: continue
        ans = ans * math.factorial(len(L)) % MOD

    print(ans%MOD)


if __name__ == "__main__":
    main()
