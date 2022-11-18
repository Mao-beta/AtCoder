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

import random

def bernoulli(p):
    r = random.uniform(0, 1)
    return int(r < p)


def var(a):
   sum_a = sum(a)
   len_a = len(a)
   mean_a = sum_a / len_a
   dev = []
   for a_i in a:
       d_sq = (a_i - mean_a)**2
       dev.append(d_sq)
   var = sum(dev)/len_a
   return var


def main():
    M = 21
    eps = 0.2
    N = int(M * (1+eps))


    ij2idx = {}
    idx = 0
    for i in range(N):
        for j in range(i + 1, N):
            ij2idx[(i, j)] = idx
            idx += 1

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


    def simulate_G(g):
        """shuffleなし、反転のみ"""
        g = g[:]
        for i in range(N):
            for j in range(i+1, N):
                idx = ij2idx[(i, j)]
                if random.uniform(0, 1) < eps:
                    g[idx] ^= 1

        return g


    gap = N * (N - 1) // 2 / (M - 1)
    vs = [int(gap * i) for i in range(M)]


    G = []
    # for v in vs:
    #     GG = "1" * v + "0" * (N * (N - 1) // 2 - v)
    #     GG = list(GG)
    #     GG = list(map(int, GG))
    #     G.append(GG[:])


    for i in range(N):
        G.append(make_flat_G(i))


    for i in range(len(G)):
        print(i)
        # G = make_random_G(p)
        GG = G[i][:]
        # GG.sort()
        C = count_dims(GG)
        C.sort()
        print(sum(C), C)

        for k in range(5):
            SG = simulate_G(GG)
            C = count_dims(SG)
            C.sort()
            print(sum(C), round(math.sqrt(var(C)), 3), C)



if __name__ == "__main__":
    main()
