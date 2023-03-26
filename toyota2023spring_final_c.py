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
    L, R = NMI()

    ans = 0
    for x in range(1, 1<<20):
        l = (L+x-1) // x * x
        r = R // x * x
        for a in range(l, r+1, x):
            b = a ^ x
            if a < b <= R and b % x == 0:
                # print(L, a, b, R, x)
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
