import sys
import math
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


#隣接リスト 1-index
def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def main():
    N, M = NMI()
    edges = [NLI() for _ in range(M)]
    K = NI()
    C = NLI()
    graph = make_adjlist_nond(N, edges)

    INF = 10**20

    shortest = []

    for start in C:
        queue = deque()
        queue.append(start)
        seen = [INF] * (N+1)
        seen[start] = 0
        while queue:
            now = queue.popleft()
            step = seen[now]
            for goto in graph[now]:
                if seen[goto] > step + 1:
                    seen[goto] = step + 1
                    queue.append(goto)

        shortest.append([seen[c] for c in C])

    # bitDP
    dp = [[INF]*K for _ in range(1<<K)]
    for i in range(K):
        dp[1<<i][i] = 1

    for case in range(1<<K):
        for src in range(K):
            if dp[case][src] == INF: continue
            for dst in range(K):
                if case & (1<<dst) == 1: continue
                dp[case ^ (1<<dst)][dst] = min(dp[case ^ (1<<dst)][dst], dp[case][src] + shortest[src][dst])

    ans = min(dp[-1])
    print(-1 if ans >= INF else ans)


if __name__ == "__main__":
    main()
