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
    N, X, Y = NMI()
    A = NLI()
    A = [a % (X+Y) for a in A]
    if X <= Y:
        if max(A) >= X:
            print("First")
        else:
            print("Second")
    else:
        ok = True
        for a in A:
            if Y <= a <= X-1:
                ok = False
        if max(A) < X:
            ok = False

        if ok:
            print("First")
        else:
            print("Second")



if __name__ == "__main__":
    main()
