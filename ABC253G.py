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
    N, L, R = NMI()

    A = list(range(1, N+1))
    # 1 -> 2, 3, ... N : N-1個
    # 2 -> 3, 4, ... N-1: N-2個
    B = [0] + list(range(N-1, 0, -1))
    C = list(accumulate(B))
    l = bisect.bisect_left(C, L)
    r = bisect.bisect_left(C, R)
    # print(C)
    # print(l, r, C[l], C[r])

    if l < r:
        x = l
        K = C[l] - L + 1
        for k in range(K):
            y = N-K+1 + k
            A[x-1], A[y-1] = A[y-1], A[x-1]

        P = deque(A[l:])
        A = A[:l]
        for x in range(l+1, r):
            p = P.pop()
            A.append(p)

        A += list(P)

        x = r
        K = R - C[r-1]
        for k in range(K):
            y = x+1 + k
            A[x-1], A[y-1] = A[y-1], A[x-1]

    else:
        x = l
        # print(x+1, N+1)
        for y in range(x+1, N+1):
            now = C[l-1] + y-x
            if L <= now <= R:
                # print(x, y)
                A[x-1], A[y-1] = A[y-1], A[x-1]

    print(*A)


if __name__ == "__main__":
    main()
