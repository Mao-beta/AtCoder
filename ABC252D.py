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
    A = NLI()
    C = Counter(A)

    ans = 0
    x = 0
    xx = 0
    xy = 0
    for a in C.values():
        ans += xy * a
        xy += x * a
        x += a
        xx += a**2

    print(ans)


if __name__ == "__main__":
    main()
