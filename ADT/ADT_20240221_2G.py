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


def main():
    W, H = NMI()
    N = NI()
    PQ = EI(N)
    an = NI()
    A = [0] + NLI() + [W]
    bn = NI()
    B = [0] + NLI() + [H]

    D = defaultdict(int)
    for p, q in PQ:
        ai = bisect.bisect_left(A, p)
        bi = bisect.bisect_left(B, q)
        D[(ai, bi)] += 1

    m = min(D.values())
    if len(D) < (an+1) * (bn+1):
        m = 0
    M = max(D.values())
    print(m, M)


if __name__ == "__main__":
    main()
