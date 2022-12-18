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
    A.sort()

    def f(x):
        idx = bisect.bisect_right(A, 2*x)
        res = x * idx + sum(A[idx:]) - x * (N - idx)
        return res / N


    l = 0
    r = 10**10

    for i in range(100):
        m1 = (l * 2 + r) / 3
        m2 = (l + r * 2) / 3
        f1 = f(m1)
        f2 = f(m2)
        # print(l, r)
        if f1 < f2:
            r = m2
        else:
            l = m1

    print(f(m1))


if __name__ == "__main__":
    main()
