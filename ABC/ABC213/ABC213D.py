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


def main():
    N = NI()
    edges = [NLI() for _ in range(N-1)]
    G = adjlist_nond_1to0(N, edges)
    G = [sorted(adj, reverse=True) for adj in G]

    from collections import defaultdict, deque, Counter

    def euler_tour(G, root=0):
        n = len(G)
        euler = []
        dq = deque([root])
        dq2 = deque()
        visited = [0] * n
        while dq:
            u = dq.pop()
            euler += [u]
            if visited[u]:
                continue
            for v in G[u]:
                if visited[v]:
                    dq += [v]
                # [親頂点、子頂点、子頂点、。。。]と入れていく.その後連結
                else:
                    dq2 += [v]
            dq.extend(dq2)
            dq2 = deque()
            visited[u] = 1
        return euler

    ans = euler_tour(G)
    ans = [a+1 for a in ans]
    print(*ans)


if __name__ == "__main__":
    main()
