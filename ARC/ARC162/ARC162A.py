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


def solve(N, P):
    # P = [[p, i] for i, p in enumerate(P)]
    # P.sort()
    # P = [i for p, i in P]

    res = 0
    for i in range(N):
        ok = True
        for j in range(i+1, N):
            # print(i, j, P[i], P[j])
            if P[i] > P[j]:
                # print("lose", i, j, P[i], P[j])
                ok = False
            if not ok:
                break
        if ok:
            res += 1

    return res


def main():
    T = NI()
    for _ in range(T):
        N = NI()
        P = NLI()
        res = solve(N, P)
        print(res)


if __name__ == "__main__":
    main()
