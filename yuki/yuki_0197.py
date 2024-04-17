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
    S = SI()
    N = NI()
    T = SI()

    if N == 0:
        if S == T:
            print("FAILURE")
        else:
            print("SUCCESS")
        return

    X = {S}
    for i in range(1, 10):
        Y = set()
        for x in X:
            a, b, c = x
            Y.add(b+a+c)
            Y.add(a+c+b)
        X = Y
        if i == N:
            break

    if T in X:
        print("FAILURE")
    else:
        print("SUCCESS")


if __name__ == "__main__":
    main()
