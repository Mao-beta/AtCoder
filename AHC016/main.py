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

    # N = 100
    # N = M
    N = min(int(M * (1+eps)), 100)
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

    def bernoulli(p):
        r = random.uniform(0, 1)
        return int(r < p)

    def make_random_G(p):
        G = [bernoulli(p) for i in range(N*(N-1)//2)]
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
        # gdim = [d * (1-eps) + (N-1-d) * eps for d in gdim]
        gdim = sorted(gdim)
        hdim = sorted(hdim)
        return sum([abs(g-h) for g, h in zip(gdim, hdim)])


    # gap = (N-1) / (M-1)
    # vs = [int(gap * i) for i in range(M)]
    #
    # G = []
    # for vnum in vs:
    #     GG = [[0]*N for _ in range(N)]
    #     for i in range(vnum):
    #         for j in range(N):
    #             GG[i][j] = 1
    #             GG[j][i] = 1
    #
    #     # print(*GG, sep="\n")
    #     GG = D2G(GG)
    #     G.append(GG[:])

    gap = N * (N - 1) // 2 / (M - 1)
    vs = [int(gap * i) for i in range(M)]

    G = []
    for v in vs:
        GG = [1] * v + [0] * (N * (N - 1) // 2 - v)
        G.append(GG[:])


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


    def simulate_G(sk):
        """shuffleなし、反転のみ"""
        g = G[sk][:]
        for i in range(N):
            for j in range(i+1, N):
                idx = ij2idx[(i, j)]
                if random.uniform(0, 1) < eps:
                    g[idx] ^= 1

        return g

    monte_K = 35

    # Gdims_monte[i]: Giから作成したシミュレーション
    Gdims_monte = [[] for _ in range(M)]
    for sk in range(M):
        for i in range(monte_K):
            G_sk_i = simulate_G(sk)
            Gdims_monte[sk].append(count_dims(G_sk_i))


    sks = []
    answers = []
    gdim_totals = []
    for i, gdims in enumerate(Gdims_monte):
        gdim_total = [0] * N

        for j, gdim in enumerate(gdims):
            for k, d in enumerate(gdim):
                gdim_total[k] += gdim[k]

        gdim_totals.append(gdim_total)


    for q in range(100):
        if IS_LOCAL:
            sk = NI()
            sks.append(sk)
            H = simulate_H(sk)
        else:
            H = input()
            H = list(map(int, H))

        hdim = count_dims(H)
        for i in range(N):
            hdim[i] *= monte_K

        res = []

        for i in range(M):
            res.append(calc_abs(gdim_totals[i], hdim))


        # res.sort()
        # C = Counter([i for a, i in res[:monte_K]])
        # ans = C.most_common()[0][0]

        ans = -1
        best = 10**8
        for i, a in enumerate(res):
            if a < best:
                ans = i
                best = a

        print(ans)
        answers.append(ans)
        sys.stdout.flush()


    if IS_LOCAL:
        bad = sum([int(sk != tk) for sk, tk in zip(sks, answers)])
        score = round((10**9) * (0.9 ** bad) / N)
        print(score)


if __name__ == "__main__":
    main()
