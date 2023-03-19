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


def adjlist(n, edges, directed=False, in_origin=1):
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


class LCATree:
    def __init__(self, n, edges, root):
        """
        最小共通祖先(LCA)を求める木　要deque
        :param n: nodeの数(1からn)
        :param edges: 辺の情報(1からn-1)
        :param root: 根
        """
        self.n = n
        self.max_double = len(bin(self.n))  # 最大何回ダブリングで遡るか およそlog2(n)
        self.adj = self.make_adjlist_nond(self.n, edges)  # 隣接リスト
        self.root = root
        # parent[i][x]はxから2^i回根の方向に上った点 -1ならその親が存在しない
        self.parent = [[-1] * (self.n + 1) for _ in range(self.max_double)]
        self.depth = [-1] * (self.n + 1)
        # ノードvを何番目に見たか（1-index）
        self.v2i = {}

        # dfsで各ノードの親と深さを記録
        stack = deque()
        stack.append(self.root)
        self.depth[self.root] = 0
        idx = 1
        while stack:
            now = stack.pop()
            par = self.parent[0][now]
            self.v2i[now] = idx
            idx += 1

            for goto in self.adj[now]:
                if goto == par:
                    continue
                stack.append(goto)
                self.parent[0][goto] = now
                self.depth[goto] = self.depth[now] + 1

        for d in range(self.max_double):
            if d == 0: continue
            pre_par = self.parent[d - 1]
            for i in range(self.n + 1):
                if pre_par[i] < 0:
                    self.parent[d][i] = -1
                    continue
                self.parent[d][i] = pre_par[pre_par[i]]

    def get_dist(self, x, y, lca):
        return self.depth[x] + self.depth[y] - self.depth[lca] * 2

    def get_LCA(self, x, y):
        """
        ノードxとノードyのLCA(最小共通祖先)を返す
        :param x:
        :param y:
        :return: res
        """
        dx, dy = self.depth[x], self.depth[y]
        # 深いほうをxとする
        if dx < dy:
            x, y = y, x
            dx, dy = dy, dx
        gap_d = dx - dy
        # 同じ高さまで引き上げる
        for i in range(self.max_double + 1):
            if (gap_d >> i) & 1:
                x = self.parent[i][x]
        # 引き上げた結果同じ所ならそこがLCA
        if x == y:
            return x

        # xとyを同時にダブリングで引き上げる
        # ジャンプ先の地点が異なるならOK、同じならジャンプ幅を半分にする
        for i in range(self.max_double - 1, -1, -1):
            if self.parent[i][x] != self.parent[i][y]:
                x = self.parent[i][x]
                y = self.parent[i][y]
        # ギリギリ同じにならない地点の親がLCA
        return self.parent[0][x]

    @staticmethod
    def make_adjlist_nond(n, edges):
        res = [[] for _ in range(n + 1)]
        for edge in edges:
            res[edge[0]].append(edge[1])
            res[edge[1]].append(edge[0])
        return res


class BIT():
    """
    BIT 0-index  ACL for python
    add(p, x): p番目にxを加算
    get(p): p番目を取得
    sum0(r): [0:r)の和を取得
    sum(l, r): [l:r)の和を取得
    """

    def __init__(self, N):
        self.n = N
        self.data = [0 for i in range(N)]

    def add(self, p, x):
        assert 0 <= p < self.n, "0<=p<n,p={0},n={1}".format(p, self.n)
        p += 1
        while (p <= self.n):
            self.data[p - 1] += x
            p += p & -p

    def get(self, p):
        return self.sum(p, p + 1)

    def sum(self, l, r):
        assert (0 <= l and l <= r and r <= self.n), "0<=l<=r<=n,l={0},r={1},n={2}".format(l, r, self.n)
        return self.sum0(r) - self.sum0(l)

    def sum0(self, r):
        s = 0
        while (r > 0):
            s += self.data[r - 1]
            r -= r & -r
        return s

    def debug(self):
        res = [self.get(p) for p in range(self.n)]
        return res


def main():
    N = NI()
    UVW = EI(N-1)
    G = adjlist(N, UVW)
    LCA = LCATree(N, [[u, v] for u, v, w in UVW], 1)
    tree = BIT(N*2)

    InOut = [[0]*2 for _ in range(N)]

    stack = deque()
    stack.append([~0, N, 0])
    stack.append([0, N, 0])
    num = 0
    while stack:
        now, par, w = stack.pop()
        if now >= 0:
            InOut[now][0] = num
            tree.add(num, w)

            for g, gw in G[now]:
                if g == par:
                    continue
                stack.append([~g, now, gw])
                stack.append([g, now, gw])
        else:
            now = ~now
            InOut[now][1] = num
            tree.add(num, -w)

        num += 1

    # print(tree.debug())
    # print(*InOut, sep="\n")

    Q = NI()
    for _ in range(Q):
        q, *X = NMI()
        if q == 1:
            i, w_new = X
            i -= 1
            u, v, w = UVW[i]
            u, v = u-1, v-1
            u_in, u_out = InOut[u]
            v_in, v_out = InOut[v]
            # print(u_in, v_in)
            if u_in < v_in:
                tree.add(v_in, -tree.get(v_in))
                tree.add(v_in, w_new)
                tree.add(v_out, -tree.get(v_out))
                tree.add(v_out, -w_new)
            else:
                tree.add(u_in, -tree.get(u_in))
                tree.add(u_in, w_new)
                tree.add(u_out, -tree.get(u_out))
                tree.add(u_out, -w_new)
            # print(tree.debug())

        else:
            u, v = X
            lca = LCA.get_LCA(u, v) - 1
            u, v = u-1, v-1
            u_in, u_out = InOut[u]
            v_in, v_out = InOut[v]
            # print(u, v, lca, tree.sum(0, u_in), tree.sum(0, v_in) , tree.sum(0, InOut[lca][0]))
            ans = tree.sum(0, u_in+1) + tree.sum(0, v_in+1) - 2 * tree.sum(0, InOut[lca][0]+1)
            print(ans)


if __name__ == "__main__":
    main()
