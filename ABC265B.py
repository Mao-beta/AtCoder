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
    N, M, T = NMI()
    A = [0] + NLI()
    XY = [NLI() for _ in range(M)]
    B = [0] * (N+1)
    for x, y in XY:
        B[x] = y

    for i in range(1, N):
        T += B[i]
        # print(i, A[i], T)
        if T <= A[i]:
            print("No")
            exit()
        T -= A[i]
        # print(i, A[i], T)

    print("Yes")


if __name__ == "__main__":
    main()
