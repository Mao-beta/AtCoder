import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

IS_LOCAL = False
try:
    import pandas as pd
    IS_LOCAL = True
except:
    pass


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
    M, eps = SMI()
    M = int(M)
    eps = float(eps)

    N = M
    ij2idx = {}
    idx = 0
    for i in range(N):
        for j in range(i+1, N):
            ij2idx[(i, j)] = idx
            idx += 1


    def D2G(D):
        """
        距離行列をグラフ形式に
        :param D:
        :return:
        """
        N = len(D)
        G = [0] * (N * (N - 1) // 2)
        for i in range(N):
            for j in range(i+1, N):
                if D[i][j] > 0:
                    idx = ij2idx[(i, j)]
                    G[idx] = 1

        return G

    def count_dims(H):
        res = [0] * N
        for i in range(N):
            for j in range(i + 1, N):
                idx = ij2idx[(i, j)]
                if H[idx] == 1:
                    res[i] += 1
                    res[j] += 1
        return res

    def calc_abs(gdim, hdim):
        # return abs(sum(gdim) - sum(hdim))
        gdim = [d * (1-eps) + (N-1-d) * eps for d in gdim]
        gdim = sorted(gdim)
        hdim = sorted(hdim)
        return sum([abs(g-h) for g, h in zip(gdim, hdim)])


    gap = (N-1) / (M-1)
    vs = [int(gap * i) for i in range(M)]

    G = []
    Gdims = []
    for vnum in vs:
        GG = [[0]*N for _ in range(N)]
        for i in range(vnum):
            for j in range(N):
                GG[i][j] = 1
                GG[j][i] = 1

        # print(*GG, sep="\n")
        GG = D2G(GG)
        G.append(GG[:])
        Gdims.append(count_dims(GG))

    # if IS_LOCAL:
    #     print(*Gdims, sep="\n")

    print(N)
    sys.stdout.flush()
    for g in G:
        print("".join(map(str, g)))
        sys.stdout.flush()


    import random
    def simulate_H(sk):
        g = G[sk][:]
        for i in range(N):
            for j in range(i+1, N):
                idx = ij2idx[(i, j)]
                if random.uniform(0, 1) < eps:
                    g[idx] ^= 1

        newv = list(range(N))
        random.shuffle(newv)
        res = [0] * (N * (N-1) // 2)
        for i in range(N):
            for j in range(i+1, N):
                idx = ij2idx[(i, j)]
                ni = newv[i]
                nj = newv[j]
                ni, nj = min(ni, nj), max(ni, nj)
                nidx = ij2idx[(ni, nj)]
                res[idx] = g[nidx]

        return res


    for q in range(100):
        if IS_LOCAL:
            H = simulate_H(NI())
        else:
            H = input()
            H = list(map(int, H))

        hdim = count_dims(H)
        res = []
        for gdim in Gdims:
            res.append(calc_abs(gdim, hdim))

        ans = -1
        best = 10**8
        for i, a in enumerate(res):
            if a < best:
                ans = i
                best = a

        print(ans)
        sys.stdout.flush()


if __name__ == "__main__":
    main()