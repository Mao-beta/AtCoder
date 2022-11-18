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


import random

class Graphs:
    def __init__(self, M, eps, N):
        self.M = M
        self.eps = eps
        self.N = N
        self.E = N * (N-1) // 2
        self.Gs = []

        self.ij2idx = {}
        idx = 0
        for i in range(N):
            for j in range(i + 1, N):
                self.ij2idx[(i, j)] = idx
                idx += 1

        self.build_Gs()


    # 計算系
    def count_dims(self, G):
        # グラフGの各頂点の次数を数える
        res = [0] * self.N
        for i in range(self.N):
            for j in range(i + 1, self.N):
                idx = self.ij2idx[(i, j)]
                if G[idx] == 1:
                    res[i] += 1
                    res[j] += 1
        return res

    def calc_abs(self, gdim, hdim):
        # 次数のリスト同士で距離を計算
        gdim = sorted(gdim)
        hdim = sorted(hdim)
        return sum([abs(g-h) for g, h in zip(gdim, hdim)])


    def simulate_G(self, sk):
        """G[sk]をepsに従って反転したものを返す"""
        g = self.Gs[sk][:]
        for i in range(self.N):
            for j in range(i+1, self.N):
                idx = self.ij2idx[(i, j)]
                if random.uniform(0, 1) < self.eps:
                    g[idx] ^= 1
        return g

    # グラフ構築関連
    def make_flat_G(self, k):
        # k本ずつ辺を持つ
        G = [0] * (self.N * (self.N - 1) // 2)

        for s in range(0, self.N, k+1):
            for i in range(s, s+k+1):
                for j in range(i+1, s+k+1):
                    if i < self.N and j < self.N:
                        idx = self.ij2idx[(i, j)]
                        G[idx] = 1
        return G

    def make_sigmoid_G(self, v):
        # 左からv個1、それ以外は0
        return [1] * v + [0] * (self.E - v)


    def build_Gs(self):
        # 全頂点の次数をなるべく揃える 3の倍数くらい？
        step = 3
        for k in range(step, self.N - step, step):
            self.Gs.append(self.make_flat_G(k))

        gap = self.E / (self.M - len(self.Gs) - 1)
        vs = [int(gap * i) for i in range(self.M - len(self.Gs))]

        for v in vs:
            GG = [1] * v + [0] * (self.E - v)
            self.Gs.append(GG[:])


    # 出力系
    def output_Gs(self):
        print(self.N)
        sys.stdout.flush()
        for g in self.Gs:
            print("".join(map(str, g)))
            sys.stdout.flush()


def main():
    M, eps = SMI()
    M = int(M)
    eps = float(eps)
    N = min(int(M * (1+eps)), 100)

    graphs = Graphs(M, eps, N)
    graphs.output_Gs()


def _main():
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



    def bernoulli(p):
        r = random.uniform(0, 1)
        return int(r < p)

    def make_random_G(p):
        G = [bernoulli(p) for i in range(N*(N-1)//2)]
        return G

    def make_flat_G(k):
        # k本ずつ辺を持つ
        G = [0] * (N * (N - 1) // 2)

        for s in range(0, N, k+1):
            for i in range(s, s+k+1):
                for j in range(i+1, s+k+1):
                    if i < N and j < N:
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
        # gdim = [d * (1-eps) + (N-1-d) * eps for d in gdim]
        gdim = sorted(gdim)
        hdim = sorted(hdim)
        return sum([abs(g-h) for g, h in zip(gdim, hdim)])


    G = []
    # 全頂点の次数をなるべく揃える 3の倍数くらい？
    step = 3
    for k in range(step, N-step, step):
        G.append(make_flat_G(k))


    gap = N * (N - 1) // 2 / (M - len(G) - 1)
    vs = [int(gap * i) for i in range(M - len(G))]

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
