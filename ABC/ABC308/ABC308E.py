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
    S = SI()

    # Ms[i][j] [0,i)の,A[*]がjである M/Xの数
    Ms = [[0]*3 for _ in range(N+1)]
    Xs = [[0]*3 for _ in range(N+1)]

    # Msr[i][j] [i,N)の,A[*]がjである M/Xの数
    Msr = [[0]*3 for _ in range(N+1)]
    Xsr = [[0]*3 for _ in range(N+1)]

    for i in range(N):
        a = A[i]
        s = S[i]
        for j in range(3):
            Ms[i+1][j] = Ms[i][j] + int(s == "M" and a == j)
            Xs[i+1][j] = Xs[i][j] + int(s == "X" and a == j)

    for i in range(N, 0, -1):
        a = A[i-1]
        s = S[i-1]
        for j in range(3):
            Msr[i-1][j] = Msr[i][j] + int(s == "M" and a == j)
            Xsr[i-1][j] = Xsr[i][j] + int(s == "X" and a == j)


    ans = 0
    for i in range(1, N-1):
        if S[i] != "E":
            continue

        for mj in range(3):
            for xj in range(3):
                T = {mj, xj, A[i]}
                mex = 0
                for k in range(4):
                    if k not in T:
                        mex = k
                        break

                ans += Ms[i][mj] * Xsr[i+1][xj] * mex

    print(ans)


if __name__ == "__main__":
    main()
