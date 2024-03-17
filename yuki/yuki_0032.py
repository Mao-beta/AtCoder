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
    L = NI()
    M = NI()
    N = NI()
    ans = 0
    x, y = divmod(N, 25)
    M += x
    ans += y
    x, y = divmod(M, 4)
    L += x
    ans += y
    x, y = divmod(L, 10)
    ans += y
    print(ans)


if __name__ == "__main__":
    main()
