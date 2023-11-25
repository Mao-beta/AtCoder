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
    N = NI()
    S = SI()
    X = [0] * 3
    for i in range(N):
        s = S[i]
        if s == "A":
            X[0] = 1
        elif s == "B":
            X[1] = 1
        else:
            X[2] = 1
        if sum(X) == 3:
            print(i+1)
            exit()


if __name__ == "__main__":
    main()
