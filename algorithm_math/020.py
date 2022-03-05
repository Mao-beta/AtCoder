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
    A = NLI()
    ans = 0
    for a in range(N-1):
        a0 = A[a]
        for b in range(a+1, N-1):
            a1 = A[b]
            for c in range(b+1, N-1):
                a2 = A[c]
                for d in range(c+1, N-1):
                    a3 = A[d]
                    a4 = 1000 - a0 - a1 - a2 - a3
                    # print(a, b, c, d)
                    ans += A[d+1:].count(a4)
    print(ans)


if __name__ == "__main__":
    main()
