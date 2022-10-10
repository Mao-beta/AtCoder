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
    A, B = NMI()

    if A >= B:
        print(A - B)

    elif A < int(B**0.5) + 2:
        # xを全探索
        ans = 10**20
        for x in range(A):
            ax = A + x
            by = (B + ax - 1) // ax * ax
            y = by - B
            ans = min(ans, x + y)
        print(ans)

    else:
        # b+y = (a+x) * n なるnを全探索
        ans = 10**20
        for n in range(1, int(B**0.5) + 2):
            by = (B + n-1) // n * n
            y = by - B
            ax = by // n
            x = ax - A
            if x >= 0:
                ans = min(ans, x + y)
            else:
                ans = min(ans, A * n - B)

        print(ans)


if __name__ == "__main__":
    T = NI()
    for _ in range(T):
        main()
