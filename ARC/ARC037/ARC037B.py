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
def make_adjlist_d(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
    return res


#nCr
def cmb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)


def dfs(node, graph, seen, parent):
    is_cycle = False
    seen[node] = 1
    nexts = graph[node]
    for goto in nexts:
        # print(f"node={node}, goto={goto}")
        if goto == parent:
            continue
        if seen[goto]:
            is_cycle = True
            continue
        is_cycle = dfs(goto, graph, seen, node) or is_cycle

    # print(node)
    # print(is_cycle)
    return is_cycle


def main():
    N, M = NMI()
    edges = [NLI() for _ in range(M)]
    graph = make_adjlist_d(N, edges)
    seen = [0] * (N+1)
    ans = 0
    for i in range(1, N+1):
        ans += 1 if not dfs(i, graph, seen, 0) else 0
    print(ans)

if __name__ == "__main__":
    main()