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
    H, W, N = NMI()
    XY = EI(N)
    XY = [[x-1, y-1] for x, y in XY]
    H2D = [0] * H
    W2D = [0] * W
    H2L = [set() for _ in range(H)]
    W2L = [set() for _ in range(W)]
    for x, y in XY:
        H2D[x] += 1
        W2D[y] += 1
        H2L[x].add(y)
        W2L[y].add(x)
    Q = NI()
    for _ in range(Q):
        q, p = NMI()
        if q == 1:
            h = p-1
            print(H2D[h])
            H2D[h] = 0
            while H2L[h]:
                w = H2L[h].pop()
                W2D[w] -= 1
                W2L[w].discard(h)
        else:
            w = p-1
            print(W2D[w])
            W2D[w] = 0
            while W2L[w]:
                h = W2L[w].pop()
                H2D[h] -= 1
                H2L[h].discard(w)


if __name__ == "__main__":
    main()
