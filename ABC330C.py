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
    D = NI()
    ans = 10**18
    for x in range(0, 10**6 * 3):
        if x**2 > D:
            break
        y = math.isqrt(D - x**2)
        ans = min(ans, abs(x ** 2 + y ** 2 - D))
        ans = min(ans, abs(x ** 2 + (y+1) ** 2 - D))

    print(ans)


if __name__ == "__main__":
    main()
