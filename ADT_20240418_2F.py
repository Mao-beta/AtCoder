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
    Q = NI()
    b2n = [[] for _ in range(N+1)]
    n2b = [set() for _ in range(200001)]
    for _ in range(Q):
        q, *X = NMI()
        if q == 1:
            i, j = X
            b2n[j].append(i)
            n2b[i].add(j)
        elif q == 2:
            print(*sorted(list(b2n[X[0]])))
        else:
            print(*sorted(list(n2b[X[0]])))


if __name__ == "__main__":
    main()
