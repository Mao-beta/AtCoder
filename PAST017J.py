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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N = NI()
    AB = EI(N)
    AB = [[x, y+1] for x, y in AB]
    Q = NI()
    T = [NI() for _ in range(Q)]
    L = [0] * 800005
    X = []
    for a, b in AB:
        X.append(a)
        X.append(b)
    for t in T:
        X.append(t)
    Z, UZ = compress(X)
    for a, b in AB:
        a, b = Z[a], Z[b]
        L[a] += 1
        L[b] -= 1
    L = list(accumulate(L))
    for t in T:
        t = Z[t]
        print(L[t])


if __name__ == "__main__":
    main()
