import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

from heapq import heappush, heappop

INF = 10 ** 20
class Dinic:
    """ 最大流(Dinic) """


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
    N, W = NMI()
    A = [0]+NLI()
    H = []
    for _ in range(N):
        _, *C = NMI()
        H.append(C)

    s = 0
    t = N+1
    tree = Dinic(N+2)

    base = sum(A)

    # 入らない(s側の辺をカット) → Ai払う
    # 家に入る(t側の辺をカット) → W払う
    # Cikの家に入ってかつ家iに入らないことはできない：
    # iのs側、Cikのt側をカットしてもつながる向きにINF
    # つまりCik->iにINFの辺を貼る
    for i, C in enumerate(H, start=1):
        tree.add_link(s, i, A[i])
        tree.add_link(i, t, W)
        for c in C:
            tree.add_link(c, i, INF)

    print(base - tree.max_flow(s, t))


if __name__ == "__main__":
    main()
