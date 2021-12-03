import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(300000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def main():
    N = NI()
    graph = [[] for _ in range(N + 1)]
    for _ in range(N-1):
        edge = NLI()
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # dp[c][i]はノードiまで見て、そこが白0か黒1かのときの場合の数
    #dp = [[-1]*(N+1) for _ in range(2)]
    dpw = [-1]*(N+1)
    dpb = [-1]*(N+1)
    seen = [0]*(N+1)

    def rec(now):
        if seen[now]: return
        dpw[now] = 1
        dpb[now] = 1
        seen[now] = 1

        for goto in graph[now]:
            if seen[goto]: continue
            rec(goto)
            dpw[now] *= dpw[goto] + dpb[goto]
            dpw[now] %= MOD
            dpb[now] *= dpw[goto]
            dpb[now] %= MOD

    rec(1)
    ans = (dpw[1]+dpb[1]) % MOD
    print(ans)


if __name__ == "__main__":
    main()
