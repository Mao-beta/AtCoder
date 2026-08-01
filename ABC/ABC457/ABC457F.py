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
    pass


def guchoku():
    N = 8
    for P in permutations(range(1, N+1)):
        P = list(P)
        D = [0] * (N-1)
        for i in range(N-2, -1, -1):
            Q = [[P[j], j] for j in range(i, N)]
            Q.sort()
            D[i] = Q[-1][1] - Q[-2][1]
        print(P, D)


if __name__ == "__main__":
    guchoku()
