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


def solve():
    N, K, X = NMI()
    A = NLI()
    AK = [[-a, 1] for a in A]
    heapify(AK)
    while K > 0:
        a, k = heappop(AK)
        if K >= k:
            heappush(AK, [a/2, k*2])
            K -= k
        else:
            heappush(AK, [a/2, K*2])
            heappush(AK, [a, k-K])
            K = 0
    while X > 0:
        a, k = heappop(AK)
        if X > k:
            X -= k
        else:
            print(-a)
            break


def main():
    T = NI()
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
