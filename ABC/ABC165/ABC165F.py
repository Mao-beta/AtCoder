import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


def adjlist(n, edges, directed=False, in_origin=1):
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


def main():
    N = NI()
    A = NLI()
    UV = EI(N-1)
    G = adjlist(N, UV)

    # dp[i]: 長さiのLISの末尾の値として狭義最小のもの
    # prev[v]: 頂点vにより上書きされた(dpにおけるindex, 値)
    dp = [0]
    ans = [1] * N
    prevs = [[-1, -1]] * N

    def dfs(now, par):
        a = A[now]
        idx = bisect.bisect_left(dp, a)
        
        # 右端
        if idx == len(dp):
            dp.append(a)
        else:
            prevs[now] = [idx, dp[idx]]
            dp[idx] = a

        ans[now] = max(ans[now], len(dp)-1)
                    
        for goto in G[now]:
            if goto == par:
                continue
            dfs(goto, now)

        prev_idx, prev_a = prevs[now]

        if prev_idx == -1:
            dp.pop()
        else:
            dp[prev_idx] = prev_a


    dfs(0, N)

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
