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
    N, M = NMI()
    UVT = EI(M)
    UVT = [[x-1, y-1, t] for x, y, t in UVT]
    Q = NI()

    INF = 10**18
    D = [[INF]*N for _ in range(N)]
    for i in range(N):
        D[i][i] = 0
    for u, v, t in UVT:
        D[u][v] = min(D[u][v], t)
        D[v][u] = min(D[v][u], t)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

    for _ in range(Q):
        K = NI()
        B = NLI()
        B = [x-1 for x in B]
        ans = INF
        for P in permutations(B):
            tmp_u = 0
            tmp_v = 0
            now_u = 0
            now_v = 0
            for b in P:
                u, v, t = UVT[b]
                nu = min(tmp_u + D[now_u][v] + t, tmp_v + D[now_v][v] + t)
                nv = min(tmp_u + D[now_u][u] + t, tmp_v + D[now_v][u] + t)
                tmp_u, tmp_v = nu, nv
                now_u, now_v = u, v
            tmp_u += D[now_u][N-1]
            tmp_v += D[now_v][N-1]
            ans = min(ans, tmp_u, tmp_v)
        print(ans)


if __name__ == "__main__":
    main()
