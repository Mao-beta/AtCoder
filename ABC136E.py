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
    return sorted(list(res), reverse=True)


def main():
    N, K = NMI()
    A = NLI()
    D = divisors(sum(A))

    for g in D:
        B = [a % g for a in A]
        B.sort()
        R = [g - b for b in B]
        R = list(accumulate(R[::-1]))[::-1]
        B = list(accumulate(B))

        for i in range(N-1):
            if B[i] == R[i+1] and B[i] <= K:
                print(g)
                exit()

    print(1)


if __name__ == "__main__":
    main()
