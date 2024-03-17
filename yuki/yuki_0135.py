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
    X = NLI()
    X.sort()
    if N == 1:
        print(0)
        return
    INF = 10**15
    ans = INF
    for i in range(N-1):
        g = X[i+1] - X[i]
        if g > 0:
            ans = min(ans, g)
    print(ans if ans < INF else 0)


if __name__ == "__main__":
    main()
