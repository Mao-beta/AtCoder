import sys

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

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]


def main():
    N, M = NMI()
    AB = EI(M)
    AB = [[x-1, y-1] for x, y in AB]
    Q = NI()
    XY = EI(Q)
    XY = [[x-1, y-1] for x, y in XY]
    INF = M
    NG = [0] * Q
    OK = [INF] * Q
    T = [[] for _ in range(M + 1)]

    for i in range(20):
        for t in range(M+1):
            T[t] = []
        for i, (ng, ok) in enumerate(zip(NG, OK)):
            t = (ng+ok) // 2
            T[t].append(i)

        uf = UnionFind(N)
        for t, (a, b) in enumerate(AB, start=1):
            uf.unite(a, b)
            for q in T[t]:
                if uf.is_same(*XY[q]):
                    OK[q] = t
                else:
                    NG[q] = t

    for q, ok in enumerate(OK):
        if ok == M and not uf.is_same(*XY[q]):
            ok = -1
        print(ok)


if __name__ == "__main__":
    main()
