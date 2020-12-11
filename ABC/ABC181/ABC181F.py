import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
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



#隣接リスト
def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def main():
    N = NI()
    P = [NLI() for _ in range(N)]
    P.sort()

    if N == 1:
        x, y = P[0]
        print(max(100-y, 100+y))
        exit()

    ok = 0
    ng = 110

    for _ in range(20):
        mid = (ok + ng) / 2
        print(mid)
        uf = UnionFind(2*N)
        gaps_p = [(100-y, y+100) for x, y in P]
        gaps_n = []
        for i in range(N-1):
            x, y = P[i]
            s, t = P[i+1]
            g = (x-s)**2 + (y-t)**2
            gaps_n.append(g)
        for i, (up, low) in enumerate(gaps_p):
            if up >= mid*2:
                if i == 0:
                    uf.unite(0, 1)
                elif i == N-1:
                    uf.unite(2*N-3, 2*N-1)
                else:
                    uf.unite(2*i-1, 2*i+1)

            if low >= mid*2:
                if i == 0:
                    uf.unite(0, 2)
                elif i == N-1:
                    uf.unite(2*N-2, 2*N-1)
                else:
                    uf.unite(2*i, 2*i+2)
        for i, g in enumerate(gaps_n):
            if g >= (mid*2)**2:
                uf.unite(2*i+1, 2*i+2)

        if uf.is_same(0, 2*N-1):
            ok = mid
        else:
            ng = mid
    print(P)
    print([math.sqrt(x) for x in gaps_n])
    print(gaps_p)
    print(mid)



if __name__ == "__main__":
    main()
