import sys
import math
from collections import defaultdict
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
    graph = adjlist_nond_1to0(N, edges)
    ans = 0
    for i in range(N):
        adj = sorted(graph[i])
        if adj[0] > i:
            continue
        if len(adj) == 1 or adj[1] > i:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
