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
    M = NI()
    g = math.gcd(N, M)
    N, M = N//g, M//g
    m = M
    while m % 2 == 0:
        m //= 2
    while m % 5 == 0:
        m //= 5
    if m > 1:
        print(-1)
        return
    x = str(N * 10**62 // M)[::-1]
    for s in x:
        if s != "0":
            print(s)
            return


if __name__ == "__main__":
    main()
