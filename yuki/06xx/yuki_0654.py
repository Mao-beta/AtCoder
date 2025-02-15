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


def compress(S):
    """ 座標圧縮 """

    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N, M, d = NMI()
    time_set = set()
    edges = []
    for i in range(M):
        u, v, p, q, w = NMI()
        u, v = u-1, v-1
        q = q + d
        time_set.add(p)
        time_set.add(q)
        edges.append([u, v, p, q, w])
    time_zip, time_unzip = compress(time_set)
    T = len(time_zip)
    din = Dinic(N*T)
    flight_times = [[] for _ in range(N)]
    for u, v, p, q, w in edges:
        p = time_zip[p]
        q = time_zip[q]
        din.add_link(u*T+p, v*T+q, w)
        flight_times[u].append(p)
        flight_times[v].append(q)
    for n in range(N):
        flight_times[n].sort()
        f_len = len(flight_times[n])
        for f in range(f_len-1):
            p, q = flight_times[n][f], flight_times[n][f+1]
            din.add_link(n*T+p, n*T+q, INF)

    if not flight_times[0] or not flight_times[-1]:
        print(0)
        exit()

    print(din.max_flow(0*T+flight_times[0][0], (N-1)*T+flight_times[N-1][-1]))


if __name__ == "__main__":
    main()