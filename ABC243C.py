import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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
    XY = [NLI() for i in range(N)]
    S = SI()
    D = defaultdict(list)
    for i, (x, y) in enumerate(XY):
        D[y].append([x, S[i]])

    for L in D.values():
        # print(L)
        rmin = 10**10
        lmax = -1
        for x, d in L:
            if d == "R":
                rmin = min(rmin, x)
            else:
                lmax = max(lmax, x)
        # print(rmin, lmax)
        if rmin < lmax:
            print("Yes")
            exit()

    print("No")



if __name__ == "__main__":
    main()
