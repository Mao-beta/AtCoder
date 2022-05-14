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
    N, K = NMI()
    X = NLI()
    hq = []
    heapify(hq)
    for i, x in enumerate(X, start=1):
        if i <= K:
            heappush(hq, (-x, i))
        else:
            p = hq[0][0] * (-1)
            if p > x:
                heappop(hq)
                heappush(hq, (-x, i))

        if i >= K:
            print(hq[0][1])



if __name__ == "__main__":
    main()
