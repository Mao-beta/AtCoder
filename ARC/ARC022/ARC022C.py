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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


#隣接リスト 1-order
def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def make_adjlist_d(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
    return res


#nCr
def cmb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)


def main():
    N = NI()
    edges = [NLI() for _ in range(N-1)]
    graph = make_adjlist_nond(N, edges)
    print(graph)
    start = 1
    par = 0
    max_depth = [-1] * (N+1)

    def dfs(node, par):
        now_depth = 0
        res = [node, 0]
        print(node, par)
        # 自分の親以外すべてに遷移
        for goto in graph[node]:
            if goto != par:
                idx, depth = dfs(goto, node)
                if depth+1 > res[1]:
                    res[0] = idx
                    res[1] = depth+1

        print(node, par)
        # 最大の深さを返す
        return res

    dfs(start, par)








if __name__ == "__main__":
    main()