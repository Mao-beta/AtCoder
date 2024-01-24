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
    N = NI()
    M = len(bin(N-1))-2
    print(M, flush=True)
    X = [[] for _ in range(M)]
    for i in range(N):
        for k in range(M):
            if (i>>k) & 1:
                X[k].append(i)
    for x in X:
        print(len(x), *x, flush=True)
    S = SI()
    ans = int(S[::-1], 2)
    if ans == 0:
        ans = N
    print(ans, flush=True)


if __name__ == "__main__":
    main()
