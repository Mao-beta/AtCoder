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
    X = [0] * (N+1)
    for x in range(1, N+1):
        for xx in range(x, N+1, x):
            X[xx] += 1
    ans = 0
    for ab in range(1, N):
        ans += X[ab] * X[N-ab]
    print(ans)


if __name__ == "__main__":
    main()
