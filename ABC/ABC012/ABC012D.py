import sys
import math
from collections import defaultdict
from collections import deque
import heapq as hq

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, M = NMI()
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, t = NMI()
        graph[a].append([b, t])
        graph[b].append([a, t])

    ans = float("inf")
    for start in range(1, N+1):
        h = []
        hq.heapify(h)
        seen = [0] * (N+1)
        cost = [float("inf")] * (N+1)
        cost[start] = 0
        hq.heappush(h, (0, start))

        while h:
            now_cost, now = hq.heappop(h)
            if seen[now] == 1:
                continue
            seen[now] = 1
            for goto, t in graph[now]:
                if seen[goto]:
                    continue
                if now_cost + t < cost[goto]:
                    cost[goto] = now_cost + t
                    hq.heappush(h, (cost[goto], goto))

        ans = min(ans, max(cost[1:]))

    print(ans)






if __name__ == "__main__":
    main()