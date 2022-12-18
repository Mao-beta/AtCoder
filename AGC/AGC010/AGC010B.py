import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


def main():
    N = NI()
    A = NLI()
    M = N * (N+1) // 2

    if sum(A) % M:
        # print(sum(A), M)
        print("NO")
        exit()

    gaps = [A[(i+1)%N] - A[i] for i in range(N)]
    if sum(gaps) != 0:
        # print(gaps)
        print("NO")
        exit()

    K = sum(A) // M
    gaps_overK = [g > K for g in gaps]
    if any(gaps_overK):
        # print(gaps_overK)
        print("NO")
        exit()

    gaps_mod = set(g % N for g in gaps)
    if len(gaps_mod) > 1:
        # print(gaps)
        # print(gaps_mod)
        print("NO")
        exit()

    gm = gaps_mod.pop()
    if gm != K % N:
        # print(gaps)
        # print(gaps_mod)
        print("NO")
        exit()

    print("YES")


if __name__ == "__main__":
    main()
