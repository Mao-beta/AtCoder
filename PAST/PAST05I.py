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
    N, M, K = NMI()
    H = NLI()
    C = NLI()
    C = [x-1 for x in C]
    AB = [NLI() for _ in range(M)]
    AB = [[x-1, y-1] for x, y in AB]

    G = [[] for _ in range(N)]
    for a, b in AB:
        if H[a] < H[b]:
            G[a].append(b)
        else:
            G[b].append(a)

    que = deque()
    INF = 10**6
    dist = [INF] * N
    for c in C:
        que.append((c, 0))
        dist[c] = 0

    while que:
        now, d = que.popleft()
        if d > dist[now]:
            continue

        for goto in G[now]:
            if dist[goto] <= d + 1:
                continue
            dist[goto] = d + 1
            que.append((goto, d+1))

    for d in dist:
        print(d if d < INF else -1)


if __name__ == "__main__":
    main()
