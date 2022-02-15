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

import sys
readline = sys.stdin.buffer.readline


class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n

    def clear(self):
        for i in range(self.n):
            self.par[i] = -1

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


def main():
    N, M = map(int, readline().split())
    AB = [tuple(int(x) for x in readline().split()) for _ in range(M)]
    Q = int(readline())
    XYZ = [tuple(int(x) for x in readline().split()) for _ in range(Q)]

    # スコアをX以下にできるか？
    # ng = 0, ok = M, ans = ok
    oks = [M] * Q
    ngs = [0] * Q

    # 同時に二分探索
    # 辺iを追加した後にJs[i]を参照し、調べる兄弟たち(j)を特定する
    # その後oks[j] or ngs[j]を更新し、Js[(ok+ng)//2] にjをadd
    Js = [set() for _ in range(M+1)]
    Js[(oks[0]+ngs[0])//2] = set(range(Q))

    uf = UnionFind(N)
    ans = [0] * Q

    # 10**5は17回で確定できる(10**5 < 2**17)
    for _ in range(17):
        uf.clear()

        # 番号の小さい辺から追加
        for i in range(1, M+1):
            a, b = AB[i-1]
            uf.unite(a-1, b-1)
            J = Js[i]

            if not J:
                continue

            for j in list(J):
                x, y, z = XYZ[j]
                ok, ng = oks[j], ngs[j]

                # 兄弟が同じ連結成分ならそのサイズ、異なるならサイズの和
                if uf.is_same(x-1, y-1):
                    res = uf.size(x-1)
                else:
                    res = uf.size(x-1) + uf.size(y-1)

                if z <= res:
                    ok = i
                    oks[j] = ok
                else:
                    ng = i
                    ngs[j] = ng

                Js[i].discard(j)
                ni = (ok + ng) >> 1

                # 次回も今回も同じなら打ち切り
                if ni != i:
                    Js[ni].add(j)

    print("\n".join(map(str, oks)))


if __name__ == "__main__":
    main()
