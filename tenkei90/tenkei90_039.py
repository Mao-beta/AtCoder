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


def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a-1, b-1
        res[a].append(b)
        res[b].append(a)
    return res


def main():
    N = NI()
    E = [NLI() for _ in range(N-1)]
    graph = adjlist_nond_1to0(N, E)

    # 自分以下の部分木のサイズ
    dp = [-1] * N
    ans = 0

    def dfs(now, parent):
        res = 1
        for goto in graph[now]:
            if goto == parent:
                continue
            res += dfs(goto, now)
        dp[now] = res

        return res

    dfs(0, -1)
    ans = 0
    for d in dp[1:]:
        ans += d * (N-d)
    print(ans)


if __name__ == "__main__":
    main()
