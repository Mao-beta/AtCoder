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


#隣接リスト 1-order
def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append([edge[1], edge[2]])
        res[edge[1]].append([edge[0], edge[2]])
    return res


def main():
    N = NI()
    edges = [NLI() for _ in range(N-1)]
    graph = make_adjlist_nond(N, edges)
    colors = [0]*(N+1)

    def dfs(node, prev):
        for goto, dist in graph[node]:
            if goto == prev:
                continue
            colors[goto] = 1 - colors[node] if dist % 2 else colors[node]
            dfs(goto, node)

    dfs(1, 0)
    print("\n".join(map(str, colors[1:])))


if __name__ == "__main__":
    main()