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
    A = NLI()
    P = [0] * (1<<N)
    G = [[] for _ in range(1<<N)]
    for i in range(1<<N):
        t = N
        for j in range(N):
            if t == N and (i>>j) & 1 == 0:
                t = j
            if (i>>j) & 1:
                P[i] += A[j]
        for g in range(1<<t, 1<<N, 1<<(t+1)):
            if i & g:
                continue
            G[i].append(g)

    S = set()
    def dfs(state, B):
        if state == (1<<N)-1:
            S.add(B)
            return
        for g in G[state]:
            dfs(state | g, B^P[g])

    dfs(0, 0)
    print(len(S))


if __name__ == "__main__":
    main()
