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
    A = set(NLI())
    B = set(NLI())

    if len(A) != N:
        print(0)
        exit()

    if len(B) != M:
        print(0)
        exit()

    ans = 1
    usedA = 0
    usedB = 0

    for x in range(N*M, 0, -1):

        if x in A and x in B:
            ans *= 1
            usedA += 1
            usedB += 1

        elif x in A and x not in B:
            ans *= usedB
            usedA += 1

        elif x not in A and x in B:
            ans *= usedA
            usedB += 1

        else:
            ans *= usedA * usedB - (N*M - x)

        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
