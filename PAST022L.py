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

from collections import deque


def topological_sort(graph):
    """
    BFSによるトポロジカルソート O(V+E)
    :param graph: 隣接リスト
    :return: 長さnならトポソ可能、そうでなければサイクルあり
    """
    n = len(graph)
    dims = [0] * n
    for i, adj in enumerate(graph):
        for goto in adj:
            dims[goto] += 1

    que = deque()
    for i, d in enumerate(dims):
        if d == 0:
            que.append(i)

    res = []
    while que:
        now = que.popleft()
        res.append(now)

        for goto in graph[now]:
            dims[goto] -= 1
            if dims[goto] == 0:
                que.append(goto)

    return res


def main():
    N = NI()
    S = [list(SI()) for _ in range(N)]
    G = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            s, t = S[i][j], S[j][i]
            if s == "o" and t == "o":
                print("No")
                return
            if s == "x" and t == "x":
                print("No")
                return
            if s == "?" and t == "?":
                continue
            if s == "?" and t == "o":
                G[j].append(i)
            elif s == "?" and t == "x":
                G[i].append(j)
            elif s == "o" and t == "?":
                G[i].append(j)
            elif s == "x" and t == "?":
                G[j].append(i)
            elif s == "o" and t == "x":
                G[i].append(j)
            elif s == "x" and t == "o":
                G[j].append(i)

    topo = topological_sort(G)
    if len(topo) != N:
        print("No")
    else:
        R = [0] * N
        for r, t in enumerate(topo):
            R[t] = r
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if R[i] < R[j]:
                    S[i][j] = "o"
                else:
                    S[i][j] = "x"
        print("Yes")
        for row in S:
            print("".join(row))



if __name__ == "__main__":
    main()
