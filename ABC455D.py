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
    N, Q = NMI()
    CP = EI(Q)
    U = [0] * (N+1)
    D = list(range(0, -N-1, -1))
    for c, p in CP:
        d = D[c]
        if d > 0:
            U[d] = 0
        U[p] = c
        D[c] = p
    ans = [0] * (N+1)
    for x, d in enumerate(D):
        if d < 0:
            i = -d
            L = [x]
            while U[x] > 0:
                L.append(U[x])
                x = U[x]
            ans[i] = len(L)
    print(*ans[1:])


if __name__ == "__main__":
    main()
