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



class LCATree:
    def __init__(self, n, edges, root):
        """
        最小共通祖先(LCA)を求める木　要deque
        :param n: nodeの数(1からn)
        :param edges: 辺の情報(1からn-1)
        :param root: 根
        """
        self.n = n
        self.max_double = len(bin(self.n)) # 最大何回ダブリングで遡るか およそlog2(n)
        self.adj = self.make_adjlist_nond(self.n, edges) # 隣接リスト
        self.root = root
        # parent[i][x]はxから2^i回根の方向に上った点 -1ならその親が存在しない
        self.parent = [[-1] * (self.n + 1) for _ in range(self.max_double)]
        self.depth = [-1] * (self.n + 1)

        # dfsで各ノードの親と深さを記録
        stack = deque()
        stack.append(self.root)
        self.depth[self.root] = 0
        while stack:
            now = stack.pop()
            par = self.parent[0][now]

            for goto in self.adj[now]:
                if goto == par:
                    continue
                stack.append(goto)
                self.parent[0][goto] = now
                self.depth[goto] = self.depth[now] + 1

        for d in range(self.max_double):
            if d == 0: continue
            pre_par = self.parent[d-1]
            for i in range(self.n+1):
                if pre_par[i] < 0:
                    self.parent[d][i] = -1
                    continue
                self.parent[d][i] = pre_par[pre_par[i]]

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
        for i in range(self.max_double+1):
            if (gap_d >> i) & 1:
                x = self.parent[i][x]
        # 引き上げた結果同じ所ならそこがLCA
        if x == y:
            return x

        # xとyを同時にダブリングで引き上げる
        # ジャンプ先の地点が異なるならOK、同じならジャンプ幅を半分にする
        for i in range(self.max_double-1, -1, -1):
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


def main():
    N = NI()
    edges = [NLI() for _ in range(N-1)]
    Q = NI()
    querys = [NLI() for _ in range(Q)]

    tree = LCATree(N, edges, 1)

    for a, b in querys:
        LCA = tree.get_LCA(a, b)
        print(tree.depth[a] + tree.depth[b] - tree.depth[LCA]*2 + 1)


if __name__ == "__main__":
    main()