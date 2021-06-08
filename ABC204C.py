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


def dfs(start, graph, seen):
    from collections import deque

    stack = deque()
    stack.append(start)

    while stack:
        now = stack.pop()
        seen[now] = 1

        for goto in graph[now]:
            if seen[goto]:
                continue
            stack.append(goto)

    return sum(seen)


def adjlist_d_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a-1, b-1
        res[a].append(b)
    return res


def main():
    N, M = NMI()
    edges = [NLI() for _ in range(M)]
    graph = adjlist_d_1to0(N, edges)
    ans = 0
    for start in range(N):
        seen = [0] * N
        ans += dfs(start, graph, seen)
    print(ans)


if __name__ == "__main__":
    main()
