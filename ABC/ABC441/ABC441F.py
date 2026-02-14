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
    PV = EI(N)
    INF = 10**15
    dpL = [[-INF]*(M+1) for _ in range(N+1)]
    dpR = [[-INF]*(M+1) for _ in range(N+1)]
    dpL[0][0] = 0
    dpR[N][0] = 0
    for i in range(N):
        p, v = PV[i]
        for j in range(M+1):
            dpL[i+1][j] = max(dpL[i+1][j], dpL[i][j])
            if j+p <= M:
                dpL[i+1][j+p] = max(dpL[i+1][j+p], dpL[i][j] + v)
    for i in range(N, 0, -1):
        p, v = PV[i-1]
        for j in range(M+1):
            dpR[i-1][j] = max(dpR[i-1][j], dpR[i][j])
            if j+p <= M:
                dpR[i-1][j+p] = max(dpR[i-1][j+p], dpR[i][j] + v)
    for i in range(N+1):
        for j in range(1, M+1):
            dpL[i][j] = max(dpL[i][j], dpL[i][j-1])
            dpR[i][j] = max(dpR[i][j], dpR[i][j-1])
    ans = ["" for _ in range(N)]
    for i in range(N):
        p, v = PV[i]
        wo = 0
        w = 0
        for j in range(M+1):
            wo = max(wo, dpL[i][j] + dpR[i+1][M-j])
            if M >= p+j:
                w = max(w, dpL[i][j] + dpR[i+1][M-p-j] + v)
        if w < wo:
            ans[i] = "C"
        elif w > wo:
            ans[i] = "A"
        else:
            ans[i] = "B"
    print("".join(ans))


if __name__ == "__main__":
    main()
