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
    N, M, X0 = NMI()
    ABST = EI(M)
    ABST = [[x-1, y-1, w, z] for x, y, w, z in ABST]
    X = [0] * M
    X[0] = X0
    G = [[] for _ in range(N)]
    for i, (a, b, s, t) in enumerate(ABST):
        G[a].append([b, s, t, i])
        G[b].append([a, s, t, i])
    que = deque()
    a, b, s, t = ABST[0]
    que.append()


if __name__ == "__main__":
    main()
