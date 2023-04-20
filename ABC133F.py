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


class HeavyLightDecomposition:
    def __init__(self, n, G):
        """
        HL分解（Heavy-Light Decomposition）
        木構造上のパスや部分木に対するクエリを、複数のセグメント木や平衡二分木に分割し、
        それぞれのデータ構造を使って高速にクエリを処理することができる。
        木を「重い辺」(heavy edge)と「軽い辺」(light edge)に分割し、木の各頂点が最大1つの重い辺を持つようになる。
        そして、各重い辺から成るパスを分割し、それぞれのパスに対してデータ構造を構築する。
        :param n: 頂点数
        :param G: 隣接リスト(0-index)

        .order[i]: iをDFS行きがけ順に変換したときのorder
        """
        self.n = n
        self.sub_size = [1] * n
        self.par = [-1] * n

        todo = [0]
        while todo:
            v = todo.pop()
            if v >= 0:
                for u in G[v]:
                    if u != self.par[v]:
                        todo.append(~u)
                        todo.append(u)
                        self.par[u] = v
            else:
                v = ~v
                self.sub_size[self.par[v]] += self.sub_size[v]

        self.head = [-1] * n
        self.head[0] = 0
        self.order = [-1] * n
        self.heavy_child = [-1] * n
        self.inv_order = [-1] * n

        todo = [0]
        cnt = 0
        while todo:
            v = todo.pop()
            self.order[v] = cnt
            self.inv_order[cnt] = v
            cnt += 1
            mx = 0
            for u in G[v]:
                if u != self.par[v] and mx < self.sub_size[u]:
                    mx = self.sub_size[u]
                    self.heavy_child[v] = u
            for u in G[v]:
                if self.par[v] != u and self.heavy_child[v] != u:
                    self.head[u] = u
                    todo.append(u)
            if self.heavy_child[v] != -1:
                self.head[self.heavy_child[v]] = self.head[v]
                todo.append(self.heavy_child[v])

    def for_each_edge(self, u, v):
        """
        頂点uから頂点vまでの各辺に対して区間クエリを行いたいときの、[l, r)のリスト
        これらをseg.prodなどにつっこむ
        """
        paths = []
        while True:
            if self.order[u] > self.order[v]:
                u, v = v, u
            if self.head[u] != self.head[v]:
                paths.append((self.order[self.head[v]], self.order[v] + 1))
                v = self.par[self.head[v]]
            else:
                paths.append((self.order[u] + 1, self.order[v] + 1))
                return paths

    def for_each_vertex(self, u, v):
        """
        頂点uから頂点vまでの各頂点に対して区間クエリを行いたいときの、[l, r)のリスト
        これらをseg.prodなどにつっこむ
        """
        paths = []
        while True:
            if self.order[u] > self.order[v]:
                u, v = v, u
            if self.head[u] != self.head[v]:
                paths.append((self.order[self.head[v]], self.order[v] + 1))
                v = self.par[self.head[v]]
            else:
                paths.append((self.order[u], self.order[v] + 1))
                return paths


class segtree():
    n = 1
    size = 1
    log = 2
    d = [0]
    op = None
    e = 10 ** 15

    def __init__(self, V, OP, E):
        self.n = len(V)
        self.op = OP
        self.e = E
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [E for i in range(2 * self.size)]
        for i in range(self.n):
            self.d[self.size + i] = V[i]
        for i in range(self.size - 1, 0, -1):
            self.update(i)

    def set(self, p, x):
        assert 0 <= p and p < self.n
        p += self.size
        self.d[p] = x
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def get(self, p):
        assert 0 <= p and p < self.n
        return self.d[p + self.size]

    def prod(self, l, r):
        assert 0 <= l and l <= r and r <= self.n
        sml = self.e
        smr = self.e
        l += self.size
        r += self.size
        while (l < r):
            if (l & 1):
                sml = self.op(sml, self.d[l])
                l += 1
            if (r & 1):
                smr = self.op(self.d[r - 1], smr)
                r -= 1
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.d[1]

    def max_right(self, l, f):
        """
        0≤l<Nなる整数 l および条件式 f が与えられたとき、
        f(prod(l,r))=True となる最大の r を求める。
        ただし、与えられる条件式 f は次を満たす:
        ある整数 x>l に対し、f(prod(l,x))=True であるとき、
        任意の整数 l<y≤x について f(prod(l,y))=True である。また、f(e)=True である。
        ->lから右にprodを伸ばしていくとき、はじめて条件がFalseになるrをさがす
        """
        assert 0 <= l and l <= self.n
        assert f(self.e)
        if l == self.n:
            return self.n
        l += self.size
        sm = self.e
        while (1):
            while (l % 2 == 0):
                l >>= 1
            if not (f(self.op(sm, self.d[l]))):
                while (l < self.size):
                    l = 2 * l
                    if f(self.op(sm, self.d[l])):
                        sm = self.op(sm, self.d[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if (l & -l) == l:
                break
        return self.n

    def min_left(self, r, f):
        """
        0≤r<Nなる整数 r および条件式 f が与えられたとき、
        f(prod(l,r))=True となる最小の l を求める。
        ただし、与えられる条件式 f は次を満たす:
        ある整数 x<r に対し、f(prod(x,r))=True であるとき、
        任意の整数 x≤y<r について f(prod(y,r))=True である。また、f(e)=True である。
        ->rから左にprodを伸ばしていくとき、はじめて条件がFalseになるlをさがす
        """
        assert 0 <= r and r < self.n
        assert f(self.e)
        if r == 0:
            return 0
        r += self.size
        sm = self.e
        while (1):
            r -= 1
            while (r > 1 & (r % 2)):
                r >>= 1
            if not (f(self.op(self.d[r], sm))):
                while (r < self.size):
                    r = (2 * r + 1)
                    if f(self.op(self.d[r], sm)):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            if (r & -r) == r:
                break
        return 0

    def update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def __str__(self):
        return str([self.get(i) for i in range(self.n)])


def main():
    N, Q = NMI()
    ABCD = []
    C_ABDI = [[] for _ in range(N)]
    G = [[] for _ in range(N)]
    for i in range(N-1):
        a, b, c, d = NMI()
        a, b, c = a-1, b-1, c-1
        ABCD.append([a, b, c, d])
        C_ABDI[c].append([a, b, d, i])
        G[a].append(b)
        G[b].append(a)

    XYUVI = []
    for i in range(Q):
        x, y, u, v = NMI()
        XYUVI.append([x-1, y, u-1, v-1] + [i])
    
    XYUVI.sort()
    
    hld = HeavyLightDecomposition(N, G)

    V = [0] * N
    for a, b, c, d in ABCD:
        aa, bb = hld.order[a], hld.order[b]
        V[max(aa, bb)] = d

    # もともとの距離を計算する用
    seg_base = segtree(V, lambda x, y: x+y, 0)
    # いま見てる色の辺数を数える用
    seg_cnt = segtree([0]*N, lambda x, y: x+y, 0)
    # いま見てる色の元の距離だけ数える用
    seg_target = segtree([0]*N, lambda x, y: x+y, 0)
    
    ans = [0] * Q
    prev_c = -1
    targets = []

    for x, y, u, v, i in XYUVI:
        if x != prev_c:
            for t, d in targets:
                seg_cnt.set(t, 0)
                seg_target.set(t, 0)

            targets = []

            for a, b, d, ei in C_ABDI[x]:
                aa, bb = hld.order[a], hld.order[b]
                t = max(aa, bb)
                seg_cnt.set(t, 1)
                seg_target.set(t, d)
                targets.append([t, d])
            prev_c = x

        # print(u, v, N, Q)
        lrs = hld.for_each_edge(u, v)
        for l, r in lrs:
            base = seg_base.prod(l, r)
            target = seg_target.prod(l, r)
            total_y = seg_cnt.prod(l, r) * y
            ans[i] += base - target + total_y

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
