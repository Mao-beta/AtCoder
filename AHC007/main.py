import sys
import math
from collections import deque
from pathlib import Path
from heapq import heapify, heappop, heappush
import random
from collections import defaultdict
import time

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

start_time = time.time()

try:
    import numpy
    IS_LOCAL = True
except:
    IS_LOCAL = False


class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n

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

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __repr__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


N = 400
M = 1995

def dist(x1, y1, x2, y2):
    return round(math.sqrt((x1-x2)**2 + (y1-y2)**2))

INF = 2000


prev = [-2] * N

def bfs(u, v, graph):
    que = deque()
    que.append(u)
    for i in range(N):
        prev[i] = -2
    prev[u] = -1

    while que:
        now = que.popleft()

        if now == v:
            return

        for goto, i in graph[now]:
            if prev[goto] >= -1: continue
            prev[goto] = now
            que.append(goto)



def _solve(values):
    TIME_LIMIT = 1.7

    XY, UV, L = values

    D = [[INF]*N for _ in range(N)]
    hq = []
    heapify(hq)
    UV2i = [[INF]*N for _ in range(N)]

    for i in range(M):
        u, v = UV[i]
        xu, yu = XY[u]
        xv, yv = XY[v]
        d = dist(xu, yu, xv, yv)
        D[u][v] = d
        D[v][u] = d
        UV2i[u][v] = i
        UV2i[v][u] = i
        heappush(hq, [d, i, u, v])

    # Kruskalで初期解を構成
    ans = [0] * M
    uf = UnionFind(N)
    graph = [[] for _ in range(N)]
    while hq:
        d, i, u, v = heappop(hq)
        if not uf.is_same(u, v):
            ans[i] = 1
            uf.unite(u, v)
            graph[u].append([v, i])
            graph[v].append([u, i])


    for i in range(M):
        u, v = UV[i]
        l = L[i]

        if l == -1:
            l = NI()

        res = ans[i]

        # res==0のとき、lを繋げてみて、サイクルからひとつ削除
        if res == 0 and time.time() - start_time <= TIME_LIMIT:
            C_hq = [(-l, i)]
            heapify(C_hq)

            bfs(u, v, graph)
            now = v
            while prev[now] != -1:
                goto = prev[now]
                idx = UV2i[now][goto]

                if idx <= i:
                    now = goto
                    continue

                d = D[now][goto]
                heappush(C_hq, (-d*2, idx))
                now = goto

            dd, di = heappop(C_hq)
            if i == di:
                print(ans[i])
                sys.stdout.flush()
                continue

            swap_edge(i, di, graph, ans, UV)

            print(ans[i])
            sys.stdout.flush()

        else:
            print(ans[i])
            sys.stdout.flush()


    return ans


def solve(values):
    # 毎回kruskal
    TIME_LIMIT = 1.7

    XY, UV, L = values

    D = [[INF]*N for _ in range(N)]
    hq = []
    heapify(hq)
    UV2i = [[INF]*N for _ in range(N)]

    for i in range(M):
        u, v = UV[i]
        xu, yu = XY[u]
        xv, yv = XY[v]
        d = dist(xu, yu, xv, yv)
        D[u][v] = d
        D[v][u] = d
        UV2i[u][v] = i
        UV2i[v][u] = i
        heappush(hq, [d, i, u, v])

    # Kruskalで初期解を構成
    ans = [0] * M
    uf = UnionFind(N)
    graph = [[] for _ in range(N)]
    while hq:
        d, i, u, v = heappop(hq)
        if not uf.is_same(u, v):
            ans[i] = 1
            uf.unite(u, v)
            graph[u].append([v, i])
            graph[v].append([u, i])


    for i in range(M):
        u, v = UV[i]
        l = L[i]

        if l == -1:
            l = NI()
            L[i] = l

        res = ans[i]

        hq = []
        heapify(hq)

        for k in range(N):
            graph[k] = []

        uf = UnionFind(N)
        for m in range(M):
            if m <= i and ans[m]:
                u, v = UV[i]
                uf.unite(u, v)
                graph[u].append([v, m])
                graph[v].append([u, m])
            else:
                ans[m] = 0
                u, v = UV[m]
                d = D[u][v]
                heappush(hq, [d, m, u, v])

        while hq:
            d, k, u, v = heappop(hq)
            if not uf.is_same(u, v):
                ans[k] = 1
                uf.unite(u, v)
                graph[u].append([v, k])
                graph[v].append([u, k])

        print(ans[i])
        sys.stdout.flush()


    return ans


def swap_edge(i, di, graph, ans, UV):
    ans[di] = 0
    ans[i] = 1
    ud, vd = UV[di]
    for k, (node, ii) in enumerate(graph[ud]):
        if node == vd:
            # print(ud, vd, di, u, v, i, graph[ud])
            del graph[ud][k]
            break

    for k, (node, ii) in enumerate(graph[vd]):
        if node == ud:
            # print(ud, vd, di, u, v, i, graph[vd])
            del graph[vd][k]
            break

    u, v = UV[i]
    graph[u].append([v, i])
    graph[v].append([u, i])


def output_ans(ans, path=None):
    if path:
        with open(path, "w") as f:
            for row in ans:
                f.write(str(row) + "\n")
    else:
        for row in ans:
            pass
            #print(*row, sep="")


def input_values(path=None):
    if path:
        XY = []
        UV = []
        L = []
        with open(path, mode="r") as f:
            inputs = f.readlines()
            for i in range(N):
                x, y = map(int, inputs[i].split())
                XY.append([x, y])
            for i in range(M):
                u, v = map(int, inputs[N+i].split())
                UV.append([u, v])
            for i in range(M):
                l = int(inputs[N+M+i])
                L.append(l)

    else:
        XY = [NLI() for _ in range(N)]
        UV = [NLI() for _ in range(M)]
        L = [-1] * M

    return XY, UV, L


def main(file=None):
    in_path = None
    out_path = None

    if file:
        in_filename = file + ".in"
        in_path = Path("./in/") / in_filename
        out_filename = file + ".out"
        out_path = Path("./out/") / out_filename
        Path("./out/").mkdir(exist_ok=True)

    values = input_values(in_path)
    ans = solve(values)
    output_ans(ans, out_path)


if __name__ == "__main__":
    if IS_LOCAL:
        for i in range(1, 2):
            random.seed(i)
            main(str(i).zfill(3))
    else:
        main()