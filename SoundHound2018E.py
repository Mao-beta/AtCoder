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


def main():
    N, M = NMI()
    UVS = [NLI() for _ in range(M)]
    UVS = [[x-1, y-1, w] for x, y, w in UVS]



def _main():
    N, M = NMI()
    UVS = [NLI() for i in range(M)]

    G = [[] for _ in range(N)]
    for u, v, s in UVS:
        u, v = u-1, v-1
        G[u].append([v, s])
        G[v].append([u, s])


    def dfs_paint_01_color(start, graph):
        bad_edges = set()

        # 二色塗り分け
        stack = deque()
        stack.append(start)

        n = len(graph)
        colors = [-1] * n
        colors[start] = 0
        S = [0] * n
        P = [n] * n

        while stack:
            now = stack.pop()
            c = colors[now]
            ns = S[now]

            for goto, s in graph[now]:
                if P[now] == goto:
                    continue

                if colors[goto] == c:
                    now, goto = min(now, goto), max(now, goto)
                    bad_edges.add((now, goto, s))
                    continue
                elif colors[goto] == 1 - c:
                    if S[goto] + S[now] != s:
                        print(0)
                        exit()
                    continue

                stack.append(goto)
                colors[goto] = 1 - c
                S[goto] = s - ns
                P[goto] = now

        return colors, S, bad_edges


    colors, S, bad_edges = dfs_paint_01_color(0, G)

    # print(colors)
    # print(S)
    # print(bad_edges)

    gaps = [0, 0]
    fix = False

    for bu, bv, s in bad_edges:
        if not fix:
            bc = colors[bu]
            assert bc == colors[bv]
            gap = s - S[bu] - S[bv]
            if gap % 2:
                print(0)
                exit()
            gaps[bc] = gap // 2
            gaps[1-bc] = -gap // 2
            fix = True

        else:
            bc = colors[bu]
            assert bc == colors[bv]
            gap = s - S[bu] - S[bv]
            if gap % 2:
                print(0)
                exit()

            if gap // 2 != gaps[bc]:
                print(0)
                exit()

    # print(gaps)

    if fix:
        for i in range(N):
            S[i] += gaps[colors[i]]

        if min(S) > 0:
            print(1)
            exit()
        else:
            print(0)
            exit()

    else:
        A = []
        B = []
        for c, s in zip(colors, S):
            if c == 0:
                A.append(s)
            else:
                B.append(s)
        amin, amax = min(A), max(A)
        bmin, bmax = min(B), max(B)

        g = 1 - amin
        amin += g
        amax += g
        bmin -= g
        bmax -= g

        # print(A)
        # print(B)

        print(max(bmin, 0))


if __name__ == "__main__":
    main()
