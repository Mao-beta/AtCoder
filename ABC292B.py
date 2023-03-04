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
    N, Q = NMI()
    E = EI(Q)
    A = [0] * (N+1)
    for c, x in E:
        if c == 1:
            A[x] += 1
        elif c == 2:
            A[x] += 2
        else:
            if A[x] >= 2:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
