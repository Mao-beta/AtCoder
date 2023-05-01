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
    N, M = NMI()
    ABCD = [SLI() for _ in range(M)]
    G = [[0, 0] for _ in range(N+1)]
    INF = 10**6
    for a, b, c, d in ABCD:
        a, c = int(a), int(c)
        b = 1 if b == "B" else 0
        d = 1 if d == "B" else 0
        G[a][b] = c + d * INF
        G[c][d] = a + b * INF

    seen = [0] * (N+1)
    X, Y = 0, 0

    for s in range(1, N+1):
        if seen[s]:
            continue

        loop = False
        c, goto = divmod(G[s][0], INF)

        while goto != 0 and seen[goto] == 0:
            seen[goto] = 1
            c, goto = divmod(G[goto][1-c], INF)

        if seen[goto]:
            loop = True

        else:
            c, goto = divmod(G[s][1], INF)

            while goto != 0 and seen[goto] == 0:
                seen[goto] = 1
                c, goto = divmod(G[goto][1 - c], INF)

        if loop:
            X += 1
        else:
            Y += 1

    print(X, Y)



if __name__ == "__main__":
    main()
