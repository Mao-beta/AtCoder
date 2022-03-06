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


def main():
    N = NI()
    S = NLI()
    A = [[0] for _ in range(3)]
    for i in range(N-1):
        g = S[i+1] - S[i]
        A[i%3].append(A[i%3][-1] + g)

    M = [min(row) for row in A]

    for i in range(N+2):
        A[i%3][i//3] -= M[i%3]

    s = 0
    for i in range(3):
        s += A[i][0]
    G = S[0] - s

    if G < 0:
        print("No")
    else:
        print("Yes")
        for i in range(N+2):
            if i % 3 == 0:
                print(A[i%3][i//3] + G, end=" ")
            else:
                print(A[i%3][i//3], end=" ")
        print()


if __name__ == "__main__":
    main()
