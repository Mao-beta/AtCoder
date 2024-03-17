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
    D = NI()
    A = NLI()

    for i in range(D, -1, -1):
        j = i-2
        if j < 1:
            break
        x = A[i]
        A[i] = 0
        A[j] += x

    while len(A) > 1 and A[-1] == 0:
        A.pop()

    print(len(A)-1)
    print(*A)


if __name__ == "__main__":
    main()
