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
    X, Y, Z = NMI()
    if X < 0:
        X, Y, Z = -X, -Y, -Z
    if Y < 0 or Y > X:
        print(X)
        return
    if Z < Y:
        if Z < 0:
            print(abs(Z)*2 + X)
        else:
            print(X)
    else:
        print(-1)


if __name__ == "__main__":
    main()