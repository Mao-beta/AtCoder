import sys
import math
import bisect
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


import time
import random

def main():
    N = NI()
    XY = EI(N)

    START = time.time()
    LIMIT = 1.88

    E = []
    D = [[.0]*N for _ in range(N)]
    dave = 0
    for i in range(N):
        xi, yi = XY[i]
        for j in range(i+1, N):
            xj, yj = XY[j]
            d = math.sqrt((xi-xj)**2 + (yi-yj)**2)
            D[i][j] = d
            D[j][i] = d
            dave += d
            E.append([d, i, j])
    dave /= N * (N-1) / 2
    E.sort(key=lambda x: abs(x[0]-dave))

    ans = [0]
    ans_set = {0}
    now = 0
    while len(ans) < N:
        goto = N
        gap = 100000.0
        for j, d in enumerate(D[now]):
            if j in ans_set:
                continue
            if abs(d-dave) < gap:
                goto = j
                gap = abs(d-dave)
        ans.append(goto)
        ans_set.add(goto)
        now = goto


    def exs(L):
        ex2 = 0
        ex = 0
        for i in range(N):
            d = D[L[i]][L[(i+1)%N]]
            ex2 += d ** 2 / N
            ex += d / N
        return ex2, ex

    def calcvar(ex2, ex):
        return ex2 - ex ** 2

    ex2, ex = exs(ans)
    var = calcvar(ex2, ex)

    def point_swap(i, j, ex2, ex):
        # ansのijを入れ替えて、ex2とexを差分計算

        d = D[ans[i]][ans[(i + 1) % N]]
        ex2 -= d ** 2 / N
        ex -= d / N
        d = D[ans[i]][ans[(i - 1) % N]]
        ex2 -= d ** 2 / N
        ex -= d / N
        d = D[ans[(j + 1) % N]][ans[j]]
        ex2 -= d ** 2 / N
        ex -= d / N
        d = D[ans[j - 1]][ans[j]]
        ex2 -= d ** 2 / N
        ex -= d / N

        # i->i+1, j->j+1 を i->j, i+1->j+1 に
        ans[i], ans[j] = ans[j], ans[i]

        d = D[ans[i]][ans[(i + 1) % N]]
        ex2 += d ** 2 / N
        ex += d / N
        d = D[ans[i]][ans[(i - 1) % N]]
        ex2 += d ** 2 / N
        ex += d / N
        d = D[ans[(j + 1) % N]][ans[j]]
        ex2 += d ** 2 / N
        ex += d / N
        d = D[ans[j - 1]][ans[j]]
        ex2 += d ** 2 / N
        ex += d / N

        return ex2, ex


    def edge_swap(i, j, ex2, ex):
        # 2-opt
        # ans[i:j]を反転して、ex2とexを差分計算

        d = D[ans[i%N]][ans[(i - 1) % N]]
        ex2 -= d ** 2 / N
        ex -= d / N
        d = D[ans[(j - 1) % N]][ans[j%N]]
        ex2 -= d ** 2 / N
        ex -= d / N

        ans[i:j] = ans[i:j][::-1]

        d = D[ans[i%N]][ans[(i - 1) % N]]
        ex2 += d ** 2 / N
        ex += d / N
        d = D[ans[(j - 1) % N]][ans[j%N]]
        ex2 += d ** 2 / N
        ex += d / N

        return ex2, ex


    start_temp = 2
    end_temp = 0.001
    best_var = var
    best_ans = ans[:]

    def prob(new_score, old_score, temp):
        return math.exp(-(new_score-old_score)/temp)

    cnt = 0
    # 2点swapで焼きなまし
    while True:
        NOW = time.time()
        if NOW - START > LIMIT:
            break
        i = random.randint(0, N-1)
        j = random.randint(i+1, N)
        if abs(i-j) % N == 0:
            continue

        ex2_old, ex_old = ex2, ex

        ex2, ex = edge_swap(i, j, ex2, ex)

        nvar = calcvar(ex2, ex)

        temp = start_temp + (end_temp - start_temp) * (NOW - START) / LIMIT
        p = prob(nvar, var, temp)

        if random.uniform(0, 1) < p:
            var = nvar
            if var < best_var:
                best_var = var
                best_ans = ans[:]
        else:
            ans[i:j] = ans[i:j][::-1]
            ex2, ex = ex2_old, ex_old
        # if cnt % 10000 == 0:
        #     print(cnt, var, best_var)
        cnt += 1

    print(*best_ans, sep="\n")
    # print(best_var)


if __name__ == "__main__":
    main()
