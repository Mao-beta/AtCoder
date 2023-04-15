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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N = NI()
    Q = NI()
    B2C = [[] for _ in range(200005)]
    C2B = [set() for _ in range(200005)]

    for _ in range(Q):
        q, i, j, *_ = NLI() * 2
        if q == 1:
            B2C[j].append(i)
            C2B[i].add(j)
        elif q == 2:
            res = sorted(B2C[i])
            print(*res)
        else:
            res = sorted(list(C2B[i]))
            print(*res)


if __name__ == "__main__":
    main()
