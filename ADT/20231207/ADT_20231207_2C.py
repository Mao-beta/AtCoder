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
    A = EI(N)
    B = EI(N)

    def rotate(X):
        res = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                res[i][j] = X[N-1-j][i]
        return res

    for _ in range(4):
        ok = True
        for i in range(N):
            for j in range(N):
                if A[i][j] == 1 and A[i][j] != B[i][j]:
                    ok = False

        if ok:
            print("Yes")
            return

        A = rotate(A)

    print("No")


if __name__ == "__main__":
    main()
