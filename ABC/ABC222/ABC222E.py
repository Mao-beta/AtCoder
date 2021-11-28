import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 998244353
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


def edgedict_nond_1to0(edges):
    E_dic = {}
    for i, (u, v) in enumerate(edges):
        u, v = u-1, v-1
        E_dic[(u, v)] = i
        E_dic[(v, u)] = i
    return E_dic


def main():
    N, M, K = NMI()
    A = NLI()
    edges = [NLI() for _ in range(N-1)]
    E_dic = edgedict_nond_1to0(edges)
    graph = adjlist_nond_1to0(N, edges)
    C = [0] * (N-1)
    parents = [-1] * N


    def dfs_stack(start):
        stack = deque()
        stack.append((start, N))

        while stack:
            now, prev = stack.pop()
            for goto in graph[now]:
                if prev == goto: continue
                parents[goto] = now
                stack.append((goto, now))

        return parents


    for i in range(M-1):
        x, y = A[i]-1, A[i+1]-1
        parents = dfs_stack(x)
        now = y
        while now != x:
            par = parents[now]
            edge = E_dic[(now, par)]
            C[edge] += 1
            now = par

    X = sum(C)
    if (X-K) % 2:
        print(0)
        exit()

    S = (X-K)//2
    # Cからいくつか選んで和をSにする
    dp = [0] * 100001
    dp[0] = 1
    dp2 = [0] * 100001

    for i in range(N-1):
        for j in range(100000):
            dp2[j] = 0
            dp2[j] += dp[j]
            if j-C[i] < 0: continue
            dp2[j] += dp[j-C[i]]
            dp2[j] %= MOD
        dp, dp2 = dp2, dp

    print(dp[S] % MOD)


if __name__ == "__main__":
    main()
