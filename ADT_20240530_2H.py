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
    N, M, K = NMI()
    AB = EI(M)
    PH = EI(K)
    AB = [[x-1, y-1] for x, y in AB]
    PH = [[x-1, y] for x, y in PH]
    PH.sort(key=lambda x: -x[1])
    H2P = [[] for _ in range(N+1)]
    for p, h in PH:
        H2P[h].append(p)
    G = adjlist(N, AB, in_origin=0)

    que = deque()
    seen = [0] * N
    for h in range(N, 0, -1):
        for p in H2P[h]:
            if not seen[p]:
                que.append([p, h])
                seen[p] = 1
        while que and que[0][1] == h:
            np, nh = que.popleft()
            for g in G[np]:
                if seen[g]:
                    continue
                seen[g] = 1
                if nh > 1:
                    que.append([g, nh-1])

    print(sum(seen))
    ans = [i for i, s in enumerate(seen, start=1) if s]
    print(*ans)


if __name__ == "__main__":
    main()
