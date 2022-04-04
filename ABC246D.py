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


def f(a, b):
    return (a+b)*(a**2+b**2)


def main():
    N = NI()
    ans = float("inf")
    for a in range(10**6+1):
        ok = 10**6+1
        ng = a-1
        while abs(ok-ng) > 1:
            mid = (ok + ng) // 2
            if f(a, mid) >= N:
                ok = mid
            else:
                ng = mid
        ans = min(ans, f(a, ok))
    print(ans)


if __name__ == "__main__":
    main()
