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
    N, A, B = NMI()
    D = NLI()
    X = []
    for d in D:
        X.append(d % (A+B))
        X.append(d % (A+B) + A+B)
    X = sorted(X)
    for i in range(N):
        g = X[i+N-1] - X[i]
        if g < A:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
