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
    T = NI()
    for _ in range(T):
        A = NLI()
        P = NLI()
        less = A[0] * 2 + A[1]
        more = A[4] * 2 + A[3]
        if more >= less:
            print(0)
        else:
            gap = less - more
            ans = gap * P[3]
            if gap % 2 == 0:
                ans = min(ans, gap // 2 * P[4])
            else:
                ans = min(ans, (gap // 2 + 1) * P[4], gap // 2 * P[4] + P[3])
            print(ans)


if __name__ == "__main__":
    main()
