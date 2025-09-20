import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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


from typing import List, Tuple, Callable

# ============================ #
#  Bidirectional Segment Tree  #
# ============================ #
class BiSegTree:
    """
    Segment tree that supports *non-commutative* monoids by storing
    both left-to-right (LR) and right-to-left (RL) folds per node.

    - op(a, b): associative binary operation; means "a followed by b"
    - e: identity element

    APIs:
      set(i, x)              : point assign
      get(i)                 : point get
      fold_lr(l, r) -> Mono  : fold on [l, r) in LR order
      fold_rl(l, r) -> Mono  : fold on [l, r) in RL order (reverse)
    """
    def __init__(self, n_or_arr, op: Callable, e):
        if isinstance(n_or_arr, int):
            n = n_or_arr
            arr = None
        else:
            arr = list(n_or_arr)
            n = len(arr)
        self.n = n
        self.op = op
        self.e = e
        size = 1
        while size < n:
            size <<= 1
        self.size = size
        # data_lr[k]: fold of the segment in LR order
        # data_rl[k]: fold of the segment in RL order
        self.data_lr = [e] * (2 * size)
        self.data_rl = [e] * (2 * size)
        if arr is not None:
            for i, x in enumerate(arr):
                self.data_lr[size + i] = x
                self.data_rl[size + i] = x
            for i in range(size - 1, 0, -1):
                L, R = 2 * i, 2 * i + 1
                self.data_lr[i] = op(self.data_lr[L], self.data_lr[R])
                self.data_rl[i] = op(self.data_rl[R], self.data_rl[L])

    def set(self, i: int, x):
        i += self.size
        self.data_lr[i] = x
        self.data_rl[i] = x
        i >>= 1
        while i:
            L, R = 2 * i, 2 * i + 1
            self.data_lr[i] = self.op(self.data_lr[L], self.data_lr[R])
            self.data_rl[i] = self.op(self.data_rl[R], self.data_rl[L])
            i >>= 1

    def get(self, i: int):
        return self.data_lr[self.size + i]

    def fold_lr(self, l: int, r: int):
        """Fold on [l, r) in Left-to-Right order."""
        op, e, size = self.op, self.e, self.size
        l += size; r += size
        left, right = e, e
        while l < r:
            if l & 1:
                left = op(left, self.data_lr[l]); l += 1
            if r & 1:
                r -= 1; right = op(self.data_lr[r], right)
            l >>= 1; r >>= 1
        return op(left, right)

    def fold_rl(self, l: int, r: int):
        """Fold on [l, r) in Right-to-Left order (reverse)."""
        op, e, size = self.op, self.e, self.size
        l += size; r += size
        left, right = e, e
        while l < r:
            if l & 1:
                # RL: new left-part becomes node.rl followed by current
                left = op(self.data_rl[l], left); l += 1
            if r & 1:
                r -= 1
                # RL: right-part grows to the right in RL sense
                right = op(right, self.data_rl[r])
            l >>= 1; r >>= 1
        return op(right, left)


# ============================ #
#              HLD            #
# ============================ #
class HLD:
    """
    Heavy-Light Decomposition (0-index).
    Provides:
      parent, depth, size, heavy, head, pos, inv, tin, tout
      lca(u, v), dist(u, v), subtree_range(u)
    Build is non-recursive; pos increases along each heavy path from head to tail.
    """
    def __init__(self, n: int, adj: List[List[int]], root: int = 0):
        self.n = n
        self.adj = adj
        self.root = root
        self.parent = [-1] * n
        self.depth  = [0] * n
        self.size   = [0] * n
        self.heavy  = [-1] * n
        self.head   = [0] * n
        self.pos    = [0] * n
        self.inv    = [0] * n
        self.tin    = [0] * n
        self.tout   = [0] * n
        self._build()

    def _build(self):
        # 1) sizes & heavy (iterative DFS)
        st = [(self.root, -1, 0)]
        while st:
            u, p, state = st.pop()
            if state == 0:
                self.parent[u] = p
                self.size[u] = 1
                st.append((u, p, 1))
                for v in self.adj[u]:
                    if v == p: continue
                    self.depth[v] = self.depth[u] + 1
                    st.append((v, u, 0))
            else:
                max_sz, hv = 0, -1
                for v in self.adj[u]:
                    if v == p: continue
                    self.size[u] += self.size[v]
                    if self.size[v] > max_sz:
                        max_sz, hv = self.size[v], v
                self.heavy[u] = hv

        # 2) assign head & pos (heavy-first order)
        cur = 0
        stack = [self.root]
        while stack:
            h = stack.pop()
            u = h
            while u != -1:
                self.head[u] = h
                self.pos[u]  = cur
                self.inv[cur] = u
                self.tin[u]  = cur
                cur += 1
                # push light children to process later
                for v in self.adj[u]:
                    if v == self.parent[u] or v == self.heavy[u]:
                        continue
                    stack.append(v)
                u = self.heavy[u]
        # 3) tout as half-open
        for u in range(self.n):
            self.tout[u] = self.tin[u] + self.size[u]

    # Utilities
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

    def subtree_range(self, u: int) -> Tuple[int, int]:
        return (self.tin[u], self.tout[u])

    # Helpers for mapping values
    def reorder_by_pos_from_node_values(self, node_vals: List):
        return [node_vals[self.inv[i]] for i in range(self.n)]

    def reorder_by_pos_from_edge_values(self, edges: List[Tuple[int,int]], edge_vals: List):
        """Store each edge's value at the child's position (parent->child)."""
        arr = [None] * self.n
        for (a, b), w in zip(edges, edge_vals):
            if self.parent[a] == b:
                arr[self.pos[a]] = w
            elif self.parent[b] == a:
                arr[self.pos[b]] = w
            else:
                raise ValueError("Edge does not match parent-child relation for the chosen root.")
        # root has no incoming edge; set identity later when building BiSegTree
        return arr
# ============================ #
#   Path fold for NON-COMM     #
# ============================ #
def path_fold_noncomm(hld: HLD, seg: BiSegTree, u: int, v: int, *, edge: bool = False):
    """
    Fold values along path u -> v with a non-commutative monoid.
    Uses:
      - RL fold for the 'u-side' segments (from u upward)
      - LR fold for the 'v-side' segments (from LCA downward)
    If edge=True, the LCA node is excluded (edge path).
    """
    op, e = seg.op, seg.e
    up = e     # accumulator for u-side (u -> LCA), correct order via RL folds
    down = e   # accumulator for LCA -> v, correct order via LR folds (prepended)

    while hld.head[u] != hld.head[v]:
        if hld.depth[hld.head[u]] >= hld.depth[hld.head[v]]:
            hu = hld.head[u]
            up = op(up, seg.fold_rl(hld.pos[hu], hld.pos[u] + 1))
            u = hld.parent[hu]
        else:
            hv = hld.head[v]
            # prepend so that upper segments come before lower ones
            down = op(seg.fold_lr(hld.pos[hv], hld.pos[v] + 1), down)
            v = hld.parent[hv]

    # same head
    if hld.depth[u] >= hld.depth[v]:
        l = hld.pos[v] + (1 if edge else 0)
        up = op(up, seg.fold_rl(l, hld.pos[u] + 1))
    else:
        l = hld.pos[u] + (1 if edge else 0)
        down = op(seg.fold_lr(l, hld.pos[v] + 1), down)

    return op(up, down)


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
    AB = EI(N)
    UV = EI(N-1)
    G = adjlist(N, UV, in_origin=0)
    hld = HLD(N, G)

    def compose(P, Q):
        a1, b1 = P
        a2, b2 = Q
        return [a1 * a2 % MOD99, (b1 * a2 + b2) % MOD99]

    seg = BiSegTree(hld.reorder_by_pos_from_node_values(AB), compose, [1, 0])

    for _ in range(Q):
        q, p, c, d, _, u, v, x = NLI() * 2
        if q == 0:
            p = hld.pos[p]
            seg.set(p, [c, d])
        else:
            a, b = path_fold_noncomm(hld, seg, u, v)
            print((a * x + b) % MOD99)


if __name__ == "__main__":
    main()
