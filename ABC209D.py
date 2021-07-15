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


def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a-1, b-1
        res[a].append(b)
        res[b].append(a)
    return res


def dfs(start, graph, seen):
    from collections import deque

    stack = deque()
    stack.append(start)
    seen[start] = 0

    while stack:
        now = stack.pop()
        now_c = seen[now]

        for goto in graph[now]:
            if seen[goto] in [0, 1]:
                continue
            stack.append(goto)
            seen[goto] = 1 - now_c

    return seen


def main():
    N, Q = NMI()
    edges = [NLI() for _ in range(N-1)]
    graph = adjlist_nond_1to0(N, edges)
    querys = [NLI() for _ in range(Q)]

    colors = dfs(0, graph, [-1]*N)

    for c, d in querys:
        c, d = c-1, d-1
        if colors[c] == colors[d]:
            print("Town")
        else:
            print("Road")



if __name__ == "__main__":
    main()
