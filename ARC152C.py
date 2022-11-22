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
    M = A[-1] - A[0]
    D = set()
    for i in range(N-1):
        D.add(2*(A[i+1]-A[0]) % M)
    D.discard(0)
    g = M
    for d in D:
        g = math.gcd(g, d)

    # if g == 0:
    #     print(A[-1])
    #     exit()
    k = (M - A[0] + g - 1) // g
    print(A[0] + g * k)


if __name__ == "__main__":
    main()
