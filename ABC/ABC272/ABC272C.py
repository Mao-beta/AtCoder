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
    Odd = []
    Even = []
    for a in A:
        if a % 2:
            Odd.append(a)
        else:
            Even.append(a)
    Odd.sort()
    Even.sort()

    ans = -1
    if len(Odd) >= 2:
        ans = max(ans, Odd[-1] + Odd[-2])

    if len(Even) >= 2:
        ans = max(ans, Even[-1] + Even[-2])

    print(ans)


if __name__ == "__main__":
    main()
