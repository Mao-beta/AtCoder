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
    N = NI()
    P = NLI()

    ans = 10**20
    one = P.index(1)
    OK = list(range(1, N+1))
    L = P[one:] + P[:one]
    if L == OK:
        ans = min(ans, one)

    tmp = one + 1
    one = (one+1) % N
    LL = P[one:] + P[:one]
    if LL[::-1] == OK:
        ans = min(ans, tmp + 1)

    P = P[::-1]
    one = P.index(1)
    OK = list(range(1, N + 1))
    L = P[one:] + P[:one]
    if L == OK:
        ans = min(ans, one + 1)

    tmp = one + 1
    one = (one + 1) % N
    LL = P[one:] + P[:one]
    if LL[::-1] == OK:
        ans = min(ans, tmp + 2)


    print(ans)



if __name__ == "__main__":
    main()
