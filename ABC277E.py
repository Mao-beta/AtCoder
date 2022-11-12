import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    UVA = [NLI() for _ in range(M)]
    S = NLI()
    UVA = [[x-1, y-1, w] for x, y, w in UVA]
    S = [x-1 for x in S]

    # スイッチ前: 0～N-1  ai=1
    # スイッチ後: N～2N-1 ai=0
    G = [[] for _ in range(2*N)]
    for u, v, a in UVA:
        if a == 0:
            G[u+N].append(v+N)
            G[v+N].append(u+N)
        else:
            G[u].append(v)
            G[v].append(u)

    for s in S:
        G[s].append(s+N)
        G[s+N].append(s)

    steps = [-1] * (2*N)
    que = deque()
    que.append(0)
    steps[0] = 0
    while que:
        now = que.popleft()
        step = steps[now]
        for goto in G[now]:
            if steps[goto] != -1:
                continue

            if abs(goto - now) == N:
                que.appendleft(goto)
                steps[goto] = step
            else:
                que.append(goto)
                steps[goto] = step + 1

    ansa = steps[N-1]
    ansb = steps[2*N-1]
    if ansa == ansb == -1:
        print(-1)
    elif ansa == -1:
        print(ansb)
    elif ansb == -1:
        print(ansa)
    else:
        print(min(ansa, ansb))


if __name__ == "__main__":
    main()
