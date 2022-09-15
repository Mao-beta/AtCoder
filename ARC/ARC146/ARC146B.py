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


def adjust(a, b):
    if a <= b:
        return a

    for bi in range(32, -1, -1):
        if ((a >> bi) & 1) == 1 and ((b >> bi) & 1) == 0:
            a -= (1 << bi)

        if a <= b:
            return a


def main():
    N, M, K = NMI()
    A = NLI()

    ans = 0
    for bi in range(32, -1, -1):
        ans |= 1 << bi
        B = [adjust(a, ans) for a in A]
        m = ans * K - sum(sorted(B)[-K:])
        if m > M:
            ans -= 1 << bi

    print(ans)


if __name__ == "__main__":
    main()
