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
    N, M = NMI()
    A = NLI()
    B = NLI()
    A.sort()
    B.sort()
    ans = 0
    ai = 0
    for bi in range(M):
        b = B[bi]
        a = -1
        while ai < N:
            a = A[ai]
            ai += 1
            if a >= b:
                break
        if a < b:
            print(-1)
            return
        ans += a
    print(ans)


if __name__ == "__main__":
    main()
