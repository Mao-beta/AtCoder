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
    S = SI()
    Ms = [0] * 3
    Xs = [0] * 3
    ans = 0
    for a, s in zip(A, S):
        if s == "X":
            Xs[a] += 1
    for a, s in zip(A, S):
        if s == "M":
            Ms[a] += 1
        elif s == "X":
            Xs[a] -= 1
        else:
            for i in range(3):
                for k in range(3):
                    T = {i, a, k}
                    mex = 0
                    for x in range(4):
                        if x not in T:
                            mex = x
                            break
                    ans += mex * Ms[i] * Xs[k]
    print(ans)


if __name__ == "__main__":
    main()
