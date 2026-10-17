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


def main():
    A = SI()
    AN = len(A)
    D = EI(AN)
    N, M = NMI()
    S = [[A.index(s) for s in SI()] for i in range(N)]
    CA2X = [[0]*AN for _ in range(M)]
    CA2D = [[0]*AN for _ in range(M)]
    for i in range(N):
        for j in range(M):
            CA2X[j][S[i][j]] += 1
    for j in range(M):
        for a in range(AN):
            for b in range(AN):
                CA2D[j][a] += D[a][b] * CA2X[j][b]
    ans = [0] * N
    for i in range(N):
        for j in range(M):
            ans[i] += CA2D[j][S[i][j]]
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
