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
    A, B, T = NMI()
    ans = 10**20
    for b in range(A+1):
        if b * B >= T:
            ans = min(ans, b*B)
            break
        aA = T - b*B
        a = (aA + A-1) // A
        ans = min(ans, a*A + b*B)

    print(ans)


if __name__ == "__main__":
    main()
