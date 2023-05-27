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


def main():
    N = NI()
    UV = EI(N-1)
    UV = [[x-1, y-1] for x, y in UV]
    D = [0] * N
    G = [[] for _ in range(N)]

    for u, v in UV:
        D[u] += 1
        D[v] += 1
        G[u].append(v)
        G[v].append(u)

    start = 0
    for i, d in enumerate(D):
        if d == 1:
            start = i

    start = G[start][0]

    steps = [-1] * N
    que = deque()
    que.append(start)
    steps[start] = 0
    while que:
        now = que.popleft()
        step = steps[now]
        for goto in G[now]:
            if steps[goto] != -1:
                continue
            que.append(goto)
            steps[goto] = step + 1

    ans = []
    for i, s in enumerate(steps):
        if s % 3 == 0:
            ans.append(len(G[i]))

    ans.sort()
    print(*ans)


if __name__ == "__main__":
    main()
