import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

# sys.set_int_max_str_digits(10 ** 6)
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


# ---------- Heavy-Light Decomposition 本体 ----------
from typing import List, Callable, Iterable, Tuple, Optional
class HLD:
    """
    Heavy-Light Decomposition on a rooted tree.
    - n: number of nodes (0-indexed)
    - adj: adjacency list (undirected tree)
    - root: root node (default 0)
    Provides:
      - parent, depth, size, heavy
      - head[u]: chain head of u
      - pos[u] : position of u in the base array
      - inv[i] : node whose position is i
      - tin[u], tout[u]: subtree is [tin[u], tout[u])
      - lca(u, v)
      - segments_on_path(u, v, edge=False): list of [l, r) segments covering path u-v
      - subtree_range(u): [tin[u], tout[u])
    """
    def __init__(self, n: int, adj: List[List[int]], root: int = 0):
        self.n = n
        self.adj = adj
        self.root = root
        self.parent = [-1] * n
        self.depth = [0] * n
        self.size = [0] * n
        self.heavy = [-1] * n
        self.head = [0] * n
        self.pos = [0] * n
        self.inv = [0] * n
        self.tin = [0] * n
        self.tout = [0] * n
        self._build()

    def _build(self):
        # 1) 非再帰 DFS：parent, depth, size, heavy
        root = self.root
        stack = [(root, -1, 0)]  # (u, parent, state) state: 0=enter, 1=exit
        order = []
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                self.parent[u] = p
                if p != -1:
                    self.depth[u] = self.depth[p] + 1
                self.size[u] = 1
                self.heavy[u] = -1
                stack.append((u, p, 1))
                for v in self.adj[u]:
                    if v == p:
                        continue
                    stack.append((v, u, 0))
            else:
                # 子の size が確定している
                max_sz = 0
                for v in self.adj[u]:
                    if v == p:
                        continue
                    self.size[u] += self.size[v]
                    if self.size[v] > max_sz:
                        max_sz = self.size[v]
                        self.heavy[u] = v

        # 2) 鎖ごとに pos を振る（heavy を優先して連続化）
        cur = 0
        st = [self.root]  # 鎖の先頭（head）候補スタック
        while st:
            h = st.pop()
            u = h
            while u != -1:
                self.head[u] = h
                self.pos[u] = cur
                self.inv[cur] = u
                self.tin[u] = cur
                cur += 1
                # light child を後で処理するためスタックへ
                for v in self.adj[u]:
                    if v == self.parent[u] or v == self.heavy[u]:
                        continue
                    st.append(v)
                u = self.heavy[u]
        # 3) tout（半開）を付ける
        for u in range(self.n):
            self.tout[u] = self.tin[u] + self.size[u]

    # ---- Utility ----
    def lca(self, u: int, v: int) -> int:
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] > self.depth[self.head[v]]:
                u = self.parent[self.head[u]]
            else:
                v = self.parent[self.head[v]]
        return u if self.depth[u] < self.depth[v] else v

    def dist(self, u: int, v: int) -> int:
        w = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[w]

    def jump_up(self, u: int, k: int) -> int:
        """k steps up from u (k>=0). Returns -1 if beyond root."""
        while u != -1 and k > 0:
            h = self.head[u]
            steps = self.pos[u] - self.pos[h]
            if k <= steps:
                return self.inv[self.pos[u] - k]
            k -= steps + 1
            u = self.parent[h]
        return u  # u or -1

    def kth_on_path(self, u: int, v: int, k: int) -> int:
        """0-based from u to v: k=0 -> u, k=dist(u,v) -> v"""
        w = self.lca(u, v)
        d1 = self.depth[u] - self.depth[w]
        if k <= d1:
            return self.jump_up(u, k)
        k2 = self.depth[v] - self.depth[w]
        return self.jump_up(v, k2 - (k - d1))

    # ---- Decomposition results ----
    def segments_on_path(self, u: int, v: int, edge: bool = False) -> List[Tuple[int, int]]:
        """
        Return list of segments [l, r) (half-open) covering the path u-v.
        If edge=True, exclude LCA node (edge queries).
        """
        segs = []
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] >= self.depth[self.head[v]]:
                hu = self.head[u]
                segs.append((self.pos[hu], self.pos[u] + 1))
                u = self.parent[hu]
            else:
                hv = self.head[v]
                segs.append((self.pos[hv], self.pos[v] + 1))
                v = self.parent[hv]
        # same head
        if self.depth[u] >= self.depth[v]:
            l = self.pos[v] + (1 if edge else 0)
            r = self.pos[u] + 1
            if l < r:
                segs.append((l, r))
        else:
            l = self.pos[u] + (1 if edge else 0)
            r = self.pos[v] + 1
            if l < r:
                segs.append((l, r))
        return segs

    def subtree_range(self, u: int) -> Tuple[int, int]:
        """Return [tin[u], tout[u]) as the contiguous range of u's subtree."""
        return (self.tin[u], self.tout[u])

    # ---- Helpers for mapping values ----
    def reorder_by_pos_from_node_values(self, node_vals: List[int]) -> List[int]:
        """arr[pos[u]] = node_vals[u]"""
        return [node_vals[self.inv[i]] for i in range(self.n)]

    def reorder_by_pos_from_edge_values(self, edges: List[Tuple[int, int]], edge_vals: List[int]) -> List[int]:
        """
        Map edge values to nodes (store on the deeper endpoint).
        For each tree edge (a,b) with value w, we set arr[pos[child]] = w where parent[child] is the other.
        Root's position gets 0.
        """
        arr = [0] * self.n
        for (a, b), w in zip(edges, edge_vals):
            if self.parent[a] == b:
                arr[self.pos[a]] = w
            elif self.parent[b] == a:
                arr[self.pos[b]] = w
            else:
                raise ValueError("Edge does not match parent-child relation; ensure edges form the same tree/root.")
        arr[self.pos[self.root]] = 0
        return arr


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
    N, Q = NMI()
    A = NLI()
    UV = EI(N-1)
    G = adjlist(N, UV, in_origin=0)
    hld = HLD(N, G)
    base = hld.reorder_by_pos_from_node_values(A)
    seg = segtree(base, lambda x, y: x + y, 0)
    for _ in range(Q):
        q, p, x, _, u, v = NLI() * 2
        if q == 0:
            p = hld.pos[p]
            seg.set(p, seg.get(p) + x)
        else:
            lrs = hld.segments_on_path(u, v)
            ans = 0
            for l, r in lrs:
                ans += seg.prod(l, r)
            print(ans)


if __name__ == "__main__":
    main()
