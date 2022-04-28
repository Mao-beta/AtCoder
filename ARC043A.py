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
    N, A, B = NMI()
    S = [NI() for _ in range(N)]
    gap = max(S) - min(S)
    if gap == 0 and B != 0:
        print(-1)
        exit()
    P = B / gap
    mean = sum(S) * B / N / gap
    Q = A - mean
    print(P, Q)


if __name__ == "__main__":
    main()
