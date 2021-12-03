import sys
import math
from collections import Counter

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def dfs_paint_01_color(start, graph):
    from collections import deque

    stack = deque()
    stack.append(start)

    n = len(graph)
    colors = [-1] * n
    colors[start] = 0

    while stack:
        now = stack.pop()
        c = colors[now]

        for goto in graph[now]:
            if colors[goto] != -1:
                continue
            stack.append(goto)
            colors[goto] = 1 - c

    return colors


def main():
    N = NI()
    edges = [NLI() for _ in range(N-1)]
    graph = [[] for _ in range(N+1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    colors = dfs_paint_01_color(1, graph)
    C = Counter(colors)
    target = 0 if C[0] >= N//2 else 1

    ans = []
    for i, c in enumerate(colors):
        if i == 0: continue
        if c == target:
            ans.append(i)
        if len(ans) == N//2:
            break

    print(*ans)


if __name__ == "__main__":
    main()
