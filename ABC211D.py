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


#隣接リスト 入力1-index を 0-index に
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
    dp = [0] * N
    dp[0] = 1
    steps = [-1] * N
    steps[0] = 0
    que = deque()
    que.append(0)
    seen = set()

    while que:
        now = que.popleft()
        if now in seen:
            continue
        seen.add(now)
        now_step = steps[now]
        for goto in graph[now]:
            if 0 <= steps[goto] <= now_step: continue
            steps[goto] = now_step + 1
            dp[goto] += dp[now]
            que.append(goto)

    print(dp[N-1] % MOD)


if __name__ == "__main__":
    main()
