import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

import pulp
from pulp import *

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
    A = NLI()
    LR = EI(M)
    if N == 1:
        print(0)
        return
    G = [A[i+1]-A[i] for i in range(N-1)]
    m = LpProblem()
    B = [LpVariable(f"b{i}", lowBound=0, cat="Integar") for i in range(M)]
    m += lpSum(B)
    L = [[] for _ in range(N)]
    R = [[] for _ in range(N)]

    try:
        # 式がそもそも線形計画的でない場合にREになるよう
        for i, (l, r) in enumerate(LR):
            l -= 2
            r -= 1
            if 0 <= l < N-1:
                L[l].append(i)
            if 0 <= r < N-1:
                R[r].append(i)
        for i in range(N-1):
            formula = G[i]
            for l in L[i]:
                formula += B[l]
            for r in R[i]:
                formula -= B[r]
            m += formula >= 0
    except:
        print(-1)
        return

    status = m.solve(pulp.PULP_CBC_CMD(msg=0))

    if LpStatus[status] == "Optimal":
        print(int(value(m.objective)))
    else:
        print(-1)


if __name__ == "__main__":
    main()
