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
EI = lambda m: [NLI() for _ in range(m)]


def subset_zeta_transform(A, N, mod):
    res = A[:]
    for i in range(N):
        for j in range(1<<N):
            if j & (1<<i) == 0:
                nj = j | (1<<i)
                res[nj] += res[j]
                res[nj] %= mod
    return res


def subset_mobius_transform(A, N, mod):
    res = A[:]
    for i in range(N):
        for j in range(1<<N):
            if j & (1<<i) == 0:
                nj = j | (1<<i)
                res[nj] -= res[j]
                res[nj] %= mod
    return res


def main():
    # 解説AC
    N, Q = NMI()
    A = NLI()
    B = NLI()
    XY = EI(Q)
    NB = 1 << N

    # F[p][j]: popcountがpで、bitがjの下位集合であるA[bit]の総和
    # Gも同様
    F = [[0]*NB for _ in range(N+1)]
    G = [[0]*NB for _ in range(N+1)]
    for i, a in enumerate(A):
        p = i.bit_count()
        F[p][i] = a
    for i, b in enumerate(B):
        p = i.bit_count()
        G[p][i] = b

    for p in range(N+1):
        F[p] = subset_zeta_transform(F[p], N, MOD99)
        G[p] = subset_zeta_transform(G[p], N, MOD99)

    FG = [[0]*NB for _ in range(2*N+1)]
    for p in range(2*N+1):
        for pf in range(N+1):
            pg = p - pf
            if pg < 0 or pg > N:
                continue

            # popcountがp, bitがjの下位集合のものは、
            # F[pf][j]とG[pg][j]の pf+pg=p における畳み込み
            # jの下位集合同士をそれぞれORでとったものはjの下位集合そのものになるため
            for j in range(NB):
                FG[p][j] += F[pf][j] * G[pg][j] % MOD99
                FG[p][j] %= MOD99

        # OR畳み込みはsubset_zeta -> 各点積(今回はここで更に和の畳み込み) -> subset_mobius
        FG[p] = subset_mobius_transform(FG[p], N, MOD99)

    for x, y in XY:
        print(FG[y][x])


if __name__ == "__main__":
    main()
