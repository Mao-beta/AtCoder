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
    A = NLI()
    UV = [NLI() for _ in range(M)]
    S = [0] * N
    G = [[] for _ in range(N)]

    UV = [[x-1, y-1] for x, y in UV]
    for u, v in UV:
        G[u].append(v)
        G[v].append(u)
        S[u] += A[v]
        S[v] += A[u]

    seen = set()
    ans = 0
    hq = [[s, i] for i, s in enumerate(S)]
    heapify(hq)

    while hq:
        cost, now = heappop(hq)
        if cost > S[now]: continue
        seen.add(now)
        ans = max(ans, cost)
        for nex in G[now]:
            if nex in seen:
                continue
            S[nex] -= A[now]
            heappush(hq, [S[nex], nex])

    print(ans)


if __name__ == "__main__":
    main()
