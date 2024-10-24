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


def main():
    N, M, Q = NMI()
    ABC = EI(M)
    ABC = [[x-1, y-1, w] for x, y, w in ABC]
    querys = EI(Q)
    ok_roads = set(range(M))
    for qi, *X in querys:
        if qi == 1:
            ok_roads.discard(X[0]-1)
    INF = 10**15
    D = [[INF]*N for _ in range(N)]
    for i in range(N):
        D[i][i] = 0
    for i, (a, b, c) in enumerate(ABC):
        if i in ok_roads:
            D[a][b] = c
            D[b][a] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    querys = querys[::-1]
    ans = []

    for qi, *X in querys:
        if qi == 1:
            i = X[0]-1
            a, b, c = ABC[i]
            D[a][b] = min(D[a][b], c)
            D[b][a] = min(D[b][a], c)
            for u in range(N):
                for v in range(N):
                    D[u][v] = min(D[u][v], D[u][a] + D[a][b] + D[b][v], D[u][b] + D[b][a] + D[a][v])
        else:
            x, y = X[0]-1, X[1]-1
            ans.append(-1 if D[x][y] == INF else D[x][y])

        # print(*D, sep="\n")
        # print()

    print(*ans[::-1], sep="\n")


if __name__ == "__main__":
    main()
