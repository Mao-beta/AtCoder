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
    a, b, c = NMI()

    def f(x):
        return a * x**5 + b * x + c

    l = 1
    r = 2
    fl = f(l)
    fr = f(r)
    for i in range(50):
        m = (l + r) / 2
        fm = f(m)

        if abs(fm) < 1e-9:
            print(m)
            exit()

        if fl < 0 < fm or fm < 0 < fl:
            r = m
            fr = fm
        else:
            l = m
            fl = fm

    print(m)



if __name__ == "__main__":
    main()
