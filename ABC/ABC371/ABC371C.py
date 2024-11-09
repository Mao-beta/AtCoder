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
    N = NI()
    MG = NI()
    UV = EI(MG)
    UV = {(x-1, y-1) for x, y in UV}
    MH = NI()
    AB = EI(MH)
    AB = {(x-1, y-1) for x, y in AB}
    C = EI(N-1)
    INF = 10**10
    ans = INF
    for P in permutations(range(N)):
        # G:P[i] = H:i
        tmp = 0
        for i in range(N):
            for j in range(i+1, N):
                h = (i, j) in AB
                pi, pj = P[i], P[j]
                if pi > pj:
                    pi, pj = pj, pi
                g = (pi, pj) in UV
                if h ^ g:
                    tmp += C[i][j-i-1]
        ans = min(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
