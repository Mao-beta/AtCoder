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
    N, Q = NMI()
    G = [0] * (N+1)
    for _ in range(Q):
        l, r, x = NMI()
        l -= 1
        G[l] += x
        G[r] -= x

    def f(g):
        if g > 0:
            return "<"
        elif g < 0:
            return ">"
        else:
            return "="

    ans = list(map(f, G))
    print("".join(ans[1:-1]))


if __name__ == "__main__":
    main()
