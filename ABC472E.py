import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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



def solve(N, M, AB):
    # 奇数長のサイクル検出
    G = adjlist(N, AB)
    L = []
    C = [-1] * N

    def dfs(now, par):
        # print(now, par)
        ans = None
        L.append(now+1)
        c = C[now]
        for v in G[now]:
            if v == par:
                continue
            if C[v] == c:
                ans = L[::-1]
                idx = ans.index(v+1)
                ans = ans[:idx + 1]
                return ans
            elif C[v] == 1-c:
                continue
            else:
                C[v] = 1-c
                ans = dfs(v, now)
                if ans is not None:
                    return ans

        L.pop()
        return ans

    C[0] = 0
    ans = dfs(0, N)
    return ans


def main():
    T = NI()
    for _ in range(T):
        N, M = NMI()
        AB = EI(M)
        ans = solve(N, M, AB)
        if ans is None:
            print(-1)
        else:
            print(len(ans))
            print(*ans)


if __name__ == "__main__":
    main()
