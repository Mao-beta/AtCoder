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
    K = NI()
    T = [0] * (6*N+1)
    J = [0] * (6*N+1)
    T[0] = 1
    J[0] = 1

    def dice(X, D):
        res = [0] * (6*N+1)
        for i, x in enumerate(X):
            for d in D:
                if i+d <= 6*N:
                    res[i+d] += x / 6
        return res

    for i in range(N):
        J = dice(J, [1, 2, 3, 4, 5, 6])
        if i < K:
            T = dice(T, [4, 4, 5, 5, 6, 6])
        else:
            T = dice(T, [1, 2, 3, 4, 5, 6])

    CJ = list(accumulate([0]+J))
    ans = 0
    for i in range(1, 6*N+1):
        ans += T[i] * CJ[i]
    print(ans)


if __name__ == "__main__":
    main()
