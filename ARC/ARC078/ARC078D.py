import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


#隣接リスト 1-index
def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def main():
    N = NI()
    edges = [NLI() for _ in range(N-1)]
    graph = make_adjlist_nond(N, edges)
    B = [-1] * (N+1)
    W = [-1] * (N+1)

    # bfs black
    start = 1
    queue = deque()
    queue.append(start)
    B[start] = 0

    while queue:
        now = queue.popleft()
        now_step = B[now]

        for goto in graph[now]:
            if B[goto] != -1:
                continue
            queue.append(goto)
            B[goto] = now_step + 1

    # bfs white
    start = N
    queue = deque()
    queue.append(start)
    W[start] = 0

    while queue:
        now = queue.popleft()
        now_step = W[now]

        for goto in graph[now]:
            if W[goto] != -1:
                continue
            queue.append(goto)
            W[goto] = now_step + 1

    fennec = sum(b <= w for b, w in zip(B[1:], W[1:]))
    snuke = N - fennec

    print("Fennec" if fennec > snuke else "Snuke")


if __name__ == "__main__":
    main()
