import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N = NI()
    XH = EI(N)

    def judge(X):
        maxx, maxh = XH[0]
        # maxt = (maxh - X) / maxx
        for i in range(1, N):
            x, h = XH[i]
            if X * maxx + (maxh - X) * x >= h * maxx:
                return False
            t = (h-X) / x
            if t * maxx > maxh - X:
                maxx = x
                maxh = h
        return True

    if judge(0):
        print(-1)
        return

    ok = 10**20
    ng = 0
    for _ in range(200):
        X = (ok + ng) / 2
        if judge(X):
            ok = X
        else:
            ng = X

    print(ok)


if __name__ == "__main__":
    main()
