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
    N = NI()
    A = NLI()

    def solve_wet(X):
        res = 0
        P = [x for x in X if x > 0]
        M = [-x for x in X if x <= 0]
        P.sort()
        M.sort()
        while P and M:
            if P[-1] <= M[-1]:
                M.pop()
                continue
            res += 1
            P.pop()
            M.pop()
        res += len(P) // 2
        return res

    wet = solve_wet(A)
    dry = solve_wet([-a for a in A])
    moist = 0
    C = Counter(A)
    for i in range(1, 10**5+1):
        moist += min(C[i], C[-i])
    moist += C[0] // 2
    print(dry, wet, moist)


if __name__ == "__main__":
    main()
