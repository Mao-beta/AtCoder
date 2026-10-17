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
    A = NLI()
    Q = NI()
    LR = EI(Q)

    C = [0] * N
    for i in range(N-1):
        g = A[i+1] - A[i]
        if i % 2:
            C[i+1] = C[i] + g
        else:
            C[i+1] = C[i]

    def f(x):
        idx = bisect.bisect_left(A, x)
        res = C[idx]
        # print(x, idx, C[idx])
        if idx > 0 and idx % 2 == 0:
            res -= A[idx] - x
        return res

    for l, r in LR:
        # print(f(r), f(l))
        print(f(r) - f(l))



if __name__ == "__main__":
    main()
