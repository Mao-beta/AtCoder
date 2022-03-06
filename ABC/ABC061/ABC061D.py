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
    N, M = NMI()
    ABC = [NLI() for _ in range(M)]

    D = [10**20] * N
    D[0] = 0

    for i in range(N):
        for j in range(M):
            a, b, c = ABC[j]
            a, b = a-1, b-1
            c *= -1
            if D[b] > D[a] + c:
                D[b] = D[a] + c
                if i == N-1 and b == N-1:
                    print("inf")
                    exit()

    print(-D[-1])


if __name__ == "__main__":
    main()
