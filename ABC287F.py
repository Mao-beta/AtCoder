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


def print_err(*args):
    print(*args, file=sys.stderr)


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
    AB = EI(N-1)
    G = adjlist(N, AB)

    P = [N] * N
    CP0 = [[] for _ in range(N)]
    CP1 = [[] for _ in range(N)]
    stack = deque([~0, 0])

    while stack:
        now = stack.pop()

        if now >= 0:
            for goto in G[now]:
                if goto == P[now]:
                    continue
                P[goto] = now
                stack.append(~goto)
                stack.append(goto)

        else:
            now = ~now
            par = P[now]

            # dp[i]: 連結成分i個のときの数
            # FPSっぽく遷移
            dp0 = [1, 0]
            dp1 = [0, 1]

            for goto in G[now]:
                if goto == par:
                    continue

                cp0, cp1 = CP0[goto], CP1[goto]
                len_d = len(dp0)
                len_c = len(cp0)

                ndp0 = [0] * (len_d + len_c - 1)
                ndp1 = [0] * (len_d + len_c - 1)

                # 遷移
                for di in range(len_d):
                    for ci in range(len_c):
                        d0, d1 = dp0[di], dp1[di]
                        c0, c1 = cp0[ci], cp1[ci]

                        ndp0[di + ci] += (c0 + c1) * d0 % MOD99
                        ndp1[di + ci] += c0 * d1 % MOD99
                        if di + ci > 0:
                            ndp1[di + ci - 1] += c1 * d1 % MOD99

                        ndp0[di + ci] %= MOD99
                        ndp1[di + ci] %= MOD99
                        if di + ci > 0:
                            ndp1[di + ci - 1] %= MOD99

                dp0, ndp0 = ndp0, dp0
                dp1, ndp1 = ndp1, dp1

            CP0[now] = dp0
            CP1[now] = dp1


    dp0, dp1 = CP0[0], CP1[0]
    for i, (d0, d1) in enumerate(zip(dp0, dp1)):
        if 1 <= i <= N:
            print((d0 + d1) % MOD99)


if __name__ == "__main__":
    main()
