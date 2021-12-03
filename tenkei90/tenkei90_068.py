import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n

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
    N = NI()
    Q = NI()
    TXYV = [NLI() for _ in range(Q)]
    uf = UnionFind(N)

    ANS = []
    Vs = [-1] * N
    A0 = [0]
    A1 = [1]
    T1 = []
    for i, (t, x, y, v) in enumerate(TXYV):
        x, y = x-1, y-1
        if t == 0:
            uf.unite(x, y)
            Vs[x] = v
        else:
            T1.append([x, y, v])
            if uf.is_same(x, y):
                ANS.append(0)
            else:
                ANS.append("Ambiguous")

    for v in Vs[:-1]:
        if v >= 0:
            A0.append(v - A0[-1])
        else:
            A0.append(0)

    for v in Vs[:-1]:
        if v >= 0:
            A1.append(v - A1[-1])
        else:
            A1.append(1)

    for i, (x, y, v) in enumerate(T1):
        if ANS[i]: continue

        x0, x1 = A0[x], A1[x]
        y0, y1 = A0[y], A1[y]
        gx = x1 - x0
        gy = y1 - y0
        g = (v - x0) // gx
        ans = y0 + g * gy
        ANS[i] = ans

    print(*ANS, sep="\n")


if __name__ == "__main__":
    main()
