import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a-1, b-1
        res[a].append(b)
        res[b].append(a)
    return res


def main():
    N, M = NMI()
    edges = [NLI() for _ in range(M)]
    Q = NI()
    XY = [NLI() for _ in range(Q)]

    # 次数が K=√2M 以上の点は遅延伝播
    K = int((2*M)**0.5)
    is_large = [0] * N
    large_adjs = [[] for _ in range(N)]

    # 実際に伝播している値と、そのクエリの番号
    colors = [[1, -1] for _ in range(N)]
    # 周囲に与えるはずの値と、そのクエリの番号
    lazys = [[1, -1] for _ in range(N)]

    graph = adjlist_nond_1to0(N, edges)
    for i, adj in enumerate(graph):
        if len(adj) >= K:
            is_large[i] = 1
            for v in adj:
                large_adjs[v].append(i)

    for i, (x, y) in enumerate(XY):
        x -= 1
        c, t = colors[x]
        for adj in large_adjs[x]:
            nc, nt = lazys[adj]
            if nt > t:
                c = nc
                t = nt

        print(c)

        colors[x][0] = y
        colors[x][1] = i

        if is_large[x]:
            lazys[x][0] = y
            lazys[x][1] = i
        else:
            for adj in graph[x]:
                colors[adj][0] = y
                colors[adj][1] = i


if __name__ == "__main__":
    main()
