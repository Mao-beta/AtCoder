import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def adjlist(n, edges, directed=False, in_origin=1) -> list[list[int]]:
    if len(edges) == 0:
        return [[] for _ in range(n)]
    
    weighted = True if len(edges[0]) > 2 else False
    if in_origin == 1:
        if weighted:
            edges = [[x-1, y-1, w] for x, y, w in edges]
        else:
            edges = [[x-1, y-1] for x, y in edges]
    
    res = [[] for _ in range(n)]
    
    if weighted:
        for u, v, c in edges:
            res[u].append([v, c])
            if not directed:
                res[v].append([u, c])
    
    else:
        for u, v in edges:
            res[u].append(v)
            if not directed:
                res[v].append(u)
    
    return res


def __main():
    N, M, L = NLI()
    ABC = EI(M)
    Q = NI()
    ST = EI(Q)
    G = adjlist(N, ABC)
    ST = [[x-1, y-1] for x, y in ST]
    # dp[s][t][k]: sからtまでk回の補給でいけるときの最大の燃料
    dp = [[[-1]*(N+1) for _ in range(N)] for _ in range(N)]
    ans = [[-1]*N for _ in range(N)]
    # 回数、燃料、始点、現在地
    hq = []
    for s in range(N):
        dp[s][s][0] = L
        hq.append([0, -L, s, s])
    while hq:
        k, l, s, t = heappop(hq)
        l *= -1
        if dp[s][t][k] > l:
            continue
        if 0 <= ans[s][t] < k:
            continue
        if ans[s][t] < 0:
            ans[s][t] = k
        # print(k, l, s, t, hq)
        
        for g, c in G[t]:
            if c > L:
                continue
            if c <= l and ans[s][g] < 0 and dp[s][g][k] < l-c:
                dp[s][g][k] = l-c
                heappush(hq, [k, -(l-c), s, g])
            if l < c <= L and ans[s][g] < 0 and dp[s][g][k+1] < L-c:
                dp[s][g][k+1] = L-c
                heappush(hq, [k+1, -(L-c), s, g])

    for s, t in ST:
        print(ans[s][t])


def main():
    N, M, L = NLI()
    ABC = EI(M)
    Q = NI()
    ST = EI(Q)
    ABC = [[x-1, y-1, w] for x, y, w in ABC]
    ST = [[x - 1, y - 1] for x, y in ST]
    INF = 10**15
    D = [[INF]*N for _ in range(N)]
    for s in range(N):
        D[s][s] = 0
    for a, b, c in ABC:
        D[a][b] = c
        D[b][a] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    D2 = [[INF]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                D2[i][j] = 0
            elif D[i][j] <= L:
                D2[i][j] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D2[i][j] = min(D2[i][j], D2[i][k] + D2[k][j])
    for s, t in ST:
        print(D2[s][t]-1 if D2[s][t] < INF else -1)


if __name__ == "__main__":
    main()
