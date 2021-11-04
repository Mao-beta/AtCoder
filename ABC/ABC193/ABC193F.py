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


INF = 10**20

class Dinic:
    __slots__ = ["n", "graph", "level", "it"]

    class Edge:
        def __init__(self, to, cap, rev=None):
            self.to = to
            self.cap = cap
            self.rev = rev

    def __init__(self, n):
        self.n = n
        self.graph = [[] for i in range(n)]
        self.level = [self.n] * self.n
        self.it = [0] * self.n

    def add_edge(self, fr, to, cap=1):
        forward = self.Edge(to, cap, None)
        forward.rev = backward = self.Edge(fr, 0, forward)
        self.graph[fr].append(forward)
        self.graph[to].append(backward)

    def bfs(self, s, t):
        graph = self.graph

        for i in range(self.n):
            self.level[i] = self.n

        level = self.level
        q = deque([s])
        level[s] = 0
        while q:
            x = q.popleft()
            lx = level[x] + 1
            for e in graph[x]:
                y = e.to
                if e.cap and level[y] > lx:
                    level[y] = lx
                    if y == t:
                        return True
                    q.append(y)
        return False

    def dfs(self, s, t, f):
        graph = self.graph
        level = self.level
        it = self.it
        q = deque([t])
        while q:
            x = q[-1]
            if x == s:
                q.pop()
                for y in q:
                    cap = graph[y][it[y]].rev.cap
                    if cap < f:
                        f = cap
                for y in q:
                    e = graph[y][it[y]]
                    e.cap += f
                    e.rev.cap -= f
                return f
            lx = level[x] - 1
            while it[x] < len(graph[x]):
                e = graph[x][it[x]]
                y = e.to
                rev = e.rev
                if rev.cap == 0 or lx != level[y]:
                    it[x] += 1
                    continue
                q.append(y)
                break
            if it[x] == len(graph[x]):
                q.pop()
                level[x] = self.n
        return 0

    def flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            for i in range(self.n):
                self.it[i] = 0
            f = self.dfs(s, t, float("inf"))
            while f:
                flow += f
                f = self.dfs(s, t, float("inf"))
        return flow


def main():
    N = NI()
    C = [SI() for _ in range(N)]

    def hw2v(h, w):
        return h * N + w

    V = 5 * N**2 + 2
    tree = Dinic(V)
    z = N**2
    S = V-1
    T = V-2
    ans = 0

    for h in range(N):
        for w in range(N):
            v = hw2v(h, w)

            # 黒で塗る→R、白で塗る→B
            # 隣接が異なる色だとスコア1→は無理
            # マスのパリティで反転
            # h+w % 2 == 0のとき黒で塗る→R、白で塗る→B
            # h+w % 2 == 1のとき白で塗る→R、黒で塗る→B
            # もともと黒のマスは、白にしたらcost inf

            # 両方Rでスコア1→片方Bでコスト1
            # S->Z: cost 1 Z->X,Y: cost inf
            # 両方Bでスコア1→片方Rでコスト1
            # Z->T: cost 1 X,Y->Z: cost inf

            if C[h][w] == "B":
                if (h+w) % 2 == 0:
                    tree.add_edge(S, v, INF)
                else:
                    tree.add_edge(v, T, INF)

            elif C[h][w] == "W":
                if (h+w) % 2 == 0:
                    tree.add_edge(v, T, INF)
                else:
                    tree.add_edge(S, v, INF)

            for dh, dw in [[0, 1], [1, 0]]:
                nh, nw = h+dh, w+dw
                nv = hw2v(nh, nw)
                if nh < 0 or nh >= N or nw < 0 or nw >= N:
                    continue
                ans += 1
                tree.add_edge(S, z, 1)
                tree.add_edge(z, v, INF)
                tree.add_edge(z, nv, INF)
                z += 1
                ans += 1
                tree.add_edge(z, T, 1)
                tree.add_edge(v, z, INF)
                tree.add_edge(nv, z, INF)
                z += 1

    print(ans - tree.flow(S, T))


if __name__ == "__main__":
    main()
