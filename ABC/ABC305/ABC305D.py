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
    S = [0]
    for i in range(N-1):
        if i % 2 == 0:
            S.append(S[-1])
        else:
            S.append(S[-1] + A[i+1] - A[i])

    def f(x):
        idx = bisect.bisect_right(A, x)
        if idx % 2:
            res = S[idx-1]
        else:
            res = S[idx-1] + x - A[idx-1]
        return res

    for l, r in LR:
        print(f(r) - f(l))


if __name__ == "__main__":
    main()
