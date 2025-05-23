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
    N, M = NMI()
    C = SLI()
    D = SLI()
    P = NLI()
    X = defaultdict(lambda: P[0])
    for d, p in zip(D, P[1:]):
        X[d] = p

    ans = 0
    for c in C:
        ans += X[c]
    print(ans)


if __name__ == "__main__":
    main()
