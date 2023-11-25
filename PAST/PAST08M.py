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
    N, M = NMI()
    ABC = EI(M)
    ABC = [[x-1, y-1, w] for x, y, w in ABC]
    G = adjlist(N, ABC, in_origin=0)

    INF = 10**18

    Z = [INF]
    steps = [-1] * N
    vals = [INF] * N

    def dfs(now, par, step, val):
        steps[now] = step
        vals[now] = val

        for goto, c in G[now]:
            if goto == par:
                continue

            if steps[goto] >= 0:
                is_odd = (steps[goto] - step) % 2
                if is_odd:
                    if c != val + vals[goto]:
                        print(-1)
                        exit()
                else:
                    if step % 2 == 0:
                        z2 = c - (val + vals[goto])
                    else:
                        z2 = (val + vals[goto]) - c

                    if z2 % 2:
                        print(-1)
                        exit()

                    if Z[0] == INF:
                        Z[0] = z2 // 2
                    elif z2 // 2 != Z[0]:
                        print(-1)
                        exit()
                continue

            dfs(goto, now, step+1, c-val)

    dfs(0, N, 0, 0)
    Z = Z[0]

    if Z < INF:
        ans = [vals[i]-Z if steps[i]%2 else vals[i]+Z for i in range(N)]

        if min(ans) < 0:
            print(-1)
            exit()
        print(*ans, sep="\n")

    else:
        # 足すやつ
        Plus = [vals[i] for i in range(N) if steps[i] % 2 == 0]
        # 引くやつ
        Minus = [vals[i] for i in range(N) if steps[i] % 2]

        if min(Minus) < 0:
            print(-1)

        elif min(Plus) >= 0:
            print(*vals, sep="\n")
            exit()

        else:
            Z = abs(min(Plus))
            ans = [vals[i] - Z if steps[i] % 2 else vals[i] + Z for i in range(N)]

            if min(ans) < 0:
                print(-1)
                exit()

            print(*ans, sep="\n")


if __name__ == "__main__":
    main()
