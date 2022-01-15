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
    N, L = NMI()
    A = NLI()
    target = -1
    for i in range(1, N):
        if A[i-1] + A[i] >= L:
            target = i
            break

    if target == -1:
        print("Impossible")
    else:
        print("Possible")
        for i in range(1, target):
            print(i)
        for i in range(N-1, target-1, -1):
            print(i)


if __name__ == "__main__":
    main()
