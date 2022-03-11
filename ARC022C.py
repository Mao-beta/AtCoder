import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


def diameter(N, graph):
    """
    :param N: 木の頂点数
    :param graph: 木の隣接行列(0-index)
    :return: 直径
    """

    def dfs(start):
        depth = [-1] * N
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

    depth1 = dfs(0)
    idx1 = depth1.index(max(depth1))
    depth2 = dfs(idx1)
    idx2 = depth2.index(max(depth2))
    return idx1, idx2


def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a - 1, b - 1
        res[a].append(b)
        res[b].append(a)
    return res


def main():
    N = NI()
    AB = [NLI() for _ in range(N-1)]
    graph = adjlist_nond_1to0(N, AB)
    x, y = diameter(N, graph)
    print(x+1, y+1)


if __name__ == "__main__":
    main()
