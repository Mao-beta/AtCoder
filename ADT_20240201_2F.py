import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N, K = NMI()
    AB = [[0, 0]] + EI(N)
    A = [a for a, b in AB] + [10**10] + [0]
    Z, UZ = compress(A)

    L = [0] * (len(Z)+3)
    for a, b in AB:
        L[0] += b
        L[Z[a]] -= b
    L = list(accumulate(L))

    for i in range(len(Z)+1):
        if L[i] <= K:
            print(UZ[i]+1)
            return


if __name__ == "__main__":
    main()
