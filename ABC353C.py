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
    A = NLI()
    A.sort()
    ans = sum(A) * 2*N
    for i, a in enumerate(A):
        idx = bisect.bisect_left(A, 10**8-a)
        ans -= 10**8 * (N-idx)
        if a >= 5*10**7:
            ans -= a*2 - 10**8
        else:
            ans -= a*2
    print(ans//2)


if __name__ == "__main__":
    main()
