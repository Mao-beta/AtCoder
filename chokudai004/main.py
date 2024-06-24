import sys
import math
import bisect
import time
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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


import random

def main():
    N, *B = NMI()
    L = EI(N)
    R = EI(N)
    A = [[random.randint(L[h][w], R[h][w]) for w in range(N)] for h in range(N)]

    START = time.time()

    H2S = [0] * N
    W2S = [0] * N

    def get_score(A):
        res = 0
        for h in range(N):
            for l in range(N):
                tmp = 0
                for r in range(l+1, N+1):
                    tmp += A[h][r-1]
                    for b in B:
                        if tmp == b:
                            res += b
                            H2S[h] += b
        for w in range(N):
            for l in range(N):
                tmp = 0
                for r in range(l+1, N+1):
                    tmp += A[r-1][w]
                    for b in B:
                        if tmp == b:
                            res += b
                            W2S[w] += b
        return res

    def get_score_hw(A, h, w):
        hres = 0
        for l in range(N):
            tmp = 0
            for r in range(l + 1, N + 1):
                tmp += A[h][r - 1]
                for b in B:
                    if tmp == b:
                        hres += b
        wres = 0
        for l in range(N):
            tmp = 0
            for r in range(l + 1, N + 1):
                tmp += A[r - 1][w]
                for b in B:
                    if tmp == b:
                        wres += b
        return hres, wres


    score = get_score(A)

    start_temp = sum(B)
    end_temp = 1
    LIMIT = 2.8

    def prob(new_score, old_score, temp):
        return math.exp((new_score-old_score)/temp)


    best_A = [a[:] for a in A]
    best_score = score


    while True:
        NOW = time.time()
        if NOW - START > LIMIT:
            break
        h = random.randint(0, N-1)
        w = random.randint(0, N-1)
        x = random.randint(L[h][w], R[h][w])
        a = A[h][w]
        if a == x:
            continue
        old_score_hw = H2S[h] + W2S[w]
        A[h][w] = x
        hnew, wnew = get_score_hw(A, h, w)
        new_score_hw = hnew + wnew
        temp = start_temp + (end_temp - start_temp) * (NOW - START) / LIMIT

        if random.uniform(0, 1) < prob(new_score_hw, old_score_hw, temp):
            score += new_score_hw - old_score_hw
            H2S[h] = hnew
            W2S[w] = wnew
            # print(score)
            if score > best_score:
                best_A = [a[:] for a in A]
                best_score = score
        else:
            A[h][w] = a

    for row in best_A:
        print(*row)


if __name__ == "__main__":
    main()
