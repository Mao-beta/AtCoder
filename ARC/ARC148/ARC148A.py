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
    A.sort()
    G = []
    for i in range(N-1):
        G.append(A[i+1] - A[i])

    gcd = 0
    for g in G:
        gcd = math.gcd(gcd, g)

    if gcd > 1:
        print(1)
    else:
        ans = len(set([a % 2 for a in A]))
        print(ans)


if __name__ == "__main__":
    main()
