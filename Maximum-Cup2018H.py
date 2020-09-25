import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
INF = 10 ** 20
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


class Dinic:
    """ 最大流(Dinic) """
    INF = 10 ** 20

    def __init__(self, n):
        self.n = n
        self.links = [[] for _ in range(n)]
        self.depth = None
        self.progress = None

    def add_link(self, _from, to, cap):
        self.links[_from].append([cap, to, len(self.links[to])])
        self.links[to].append([0, _from, len(self.links[_from]) - 1])

    def bfs(self, s):
        from collections import deque

        depth = [-1] * self.n
        depth[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for cap, to, rev in self.links[v]:
                if cap > 0 and depth[to] < 0:
                    depth[to] = depth[v] + 1
                    q.append(to)
        self.depth = depth

    def dfs(self, v, t, flow):
        if v == t:
            return flow
        links_v = self.links[v]
        for i in range(self.progress[v], len(links_v)):
            self.progress[v] = i
            cap, to, rev = link = links_v[i]
            if cap == 0 or self.depth[v] >= self.depth[to]:
                continue
            d = self.dfs(to, t, min(flow, cap))
            if d == 0:
                continue
            link[0] -= d
            self.links[to][rev][0] += d
            return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.depth[t] < 0:
                return flow
            self.progress = [0] * self.n
            current_flow = self.dfs(s, t, INF)
            while current_flow > 0:
                flow += current_flow
                current_flow = self.dfs(s, t, INF)


def main():
    N, M = NMI()
    graph = [[INF]*N for _ in range(N)]
    for i in range(N):
        graph[i][i] = 0
    edges = [NLI() for _ in range(M)]
    for v, u, w in edges:
        graph[v-1][u-1] = w
        graph[u-1][v-1] = w
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    K = NI()
    A = list(map(lambda x: x-1, NMI()))
    Q = NI()
    B = list(map(lambda x: x-1, NMI()))

    ok = 10**10
    ng = -1

    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        din = Dinic(3*N + 2)
        source = 3*N
        sink = source + 1
        for a in A:
            din.add_link(source, a, 1)
            din.add_link(a+N, sink, 1)
        for b in B:
            din.add_link(source, b + 2*N, 1)

        for k in range(K-1):
            p, q = A[k], A[k+1]
            s = graph[p][q]
            if s <= mid:
                din.add_link(p, q+N, 1)
            for b in B:
                if graph[b][q] <= mid:
                    din.add_link(b+2*N, q+N, 1)
        if din.max_flow(source, sink) == K-1:
            ok = mid
        else:
            ng = mid

    print(ok)





if __name__ == "__main__":
    main()