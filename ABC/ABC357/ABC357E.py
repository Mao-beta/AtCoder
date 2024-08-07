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
    A = [x-1 for x in A]
    R = [[] for _ in range(N)]
    for i, a in enumerate(A):
        R[a].append(i)
    cnts = [0] * N
    seen = [0] * N

    def search(start):
        now = start
        V = {start}
        L = [start]
        seen[start] = 1
        while A[now] not in V:
            if cnts[A[now]] > 0 or seen[A[now]]:
                return
            seen[A[now]] = 1
            V.add(A[now])
            L.append(A[now])
            now = A[now]
        idx = L.index(A[now])
        total = len(L)
        loop = total - idx
        for v in L[idx:]:
            cnts[v] = loop

    for i in range(N):
        if cnts[i] > 0:
            continue
        search(i)

    for i in range(N):
        if cnts[i] == 0:
            continue

        D = deque()
        D.append(i)
        while D:
            now = D.pop()
            for g in R[now]:
                if cnts[g] > 0:
                    continue
                cnts[g] = cnts[now] + 1
                D.append(g)

    print(sum(cnts))


if __name__ == "__main__":
    main()
