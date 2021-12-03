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


def adjlist_d_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a-1, b-1
        res[a].append(b)
    return res


def topological_sort(graph):
    n = len(graph)
    dims = [0] * n
    for i, adj in enumerate(graph):
        for goto in adj:
            dims[goto] += 1

    que = deque()
    for i, d in enumerate(dims):
        if d == 0:
            que.append(i)

    res = []
    while que:
        now = que.popleft()
        res.append(now)

        for goto in graph[now]:
            dims[goto] -= 1
            if dims[goto] == 0:
                que.append(goto)

    return res


def main():
    N, M = NMI()
    edges = [NLI() for _ in range(M)]
    graph = adjlist_d_1to0(N, edges)

    topo = topological_sort(graph)
    if len(topo) == N:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
