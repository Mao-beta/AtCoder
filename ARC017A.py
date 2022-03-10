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


def divisors(x):
    res = set()
    for i in range(1, int(x**0.5) + 2):
        if x % i == 0:
            res.add(i)
            res.add(x//i)
    return res


def main():
    N = NI()
    D = divisors(N)
    if len(D) == 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
