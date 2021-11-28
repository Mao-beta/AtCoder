import sys
import math
from collections import deque
from heapq import heappop, heappush, heapify

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def adjlist_d_1to0(n, edges):
    res = [set() for _ in range(n)]
    for a, b in edges:
        a, b = a-1, b-1
        res[a].add(b)
    return res


def main():
    N, M = NMI()
    edges = [NLI() for _ in range(M)]
    rev_edges = [[b, a] for a, b in edges]
    graph = adjlist_d_1to0(N, edges)
    rev_graph = adjlist_d_1to0(N, rev_edges)
    D = [len(adj) for adj in rev_graph]

    hq = []
    heapify(hq)
    ans = []
    seen = [0] * N
    for i, d in enumerate(D):
        if d == 0:
            heappush(hq, i)

    if not hq:
        print(-1)
        exit()

    while hq:
        now = heappop(hq)
        seen[now] = 1
        ans.append(now+1)
        for goto in graph[now]:
            if seen[goto]:
                print(-1)
                exit()
            D[goto] -= 1
            if D[goto] == 0:
                heappush(hq, goto)

    if len(ans) != N:
        print(-1)
        exit()
    print(*ans)


if __name__ == "__main__":
    main()
