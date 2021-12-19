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
    C = list(SI().split())
    edges = [NLI() for _ in range(N-1)]
    graph = adjlist_nond_1to0(N, edges)

    # dp[i][j]: 頂点i以下の部分木について、j=0/1/2(aのみ、bのみ、両方)の場合の数
    # iを含む連結成分より下の切り離された部分は問題文の条件を満たしている前提
    dp = [[-1] * 3 for _ in range(N)]
    prev = [-1] * N

    def dfs(now):
        c = C[now]

        dp[now][0] = 1 if c == "a" else 0
        dp[now][1] = 1 if c == "b" else 0
        dp[now][2] = 1

        for goto in graph[now]:
            if goto == prev[now]: continue

            prev[goto] = now
            dfs(goto)

            if c == "a":
                dp[now][0] = dp[now][0] * (dp[goto][0] + dp[goto][2]) % MOD
                dp[now][2] = dp[now][2] * (sum(dp[goto]) + dp[goto][2]) % MOD

            else:
                dp[now][1] = dp[now][1] * (dp[goto][1] + dp[goto][2]) % MOD
                dp[now][2] = dp[now][2] * (sum(dp[goto]) + dp[goto][2]) % MOD

        dp[now][2] -= dp[now][0] + dp[now][1]
        dp[now][2] %= MOD

    dfs(0)
    print(dp[0][2])


if __name__ == "__main__":
    main()
