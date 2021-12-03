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


def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def diameter(N, graph):
    """
    :param N: 木の頂点数
    :param graph: 木の隣接行列(1-index)
    :return: 直径
    """

    def dfs(start):
        depth = [-1] * (N+1)
        depth[start] = 0

        stack = deque()
        stack.append(start)

        while stack:
            now = stack.pop()
            for goto in graph[now]:
                if depth[goto] != -1:
                    continue
                depth[goto] = depth[now] + 1
                stack.append(goto)
        return depth

    depth1 = dfs(1)
    idx = depth1.index(max(depth1))
    depth2 = dfs(idx)

    return max(depth2)


def main():
    N = NI()
    edges = [NLI() for _ in range(N-1)]
    graph = make_adjlist_nond(N, edges)
    print(diameter(N, graph) + 1)


if __name__ == "__main__":
    main()
