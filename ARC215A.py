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
    T = NI()
    for _ in range(T):
        N, K, L = NMI()
        A = NLI()
        A.sort()
        ans = 0
        l, r = A[0], L-A[-1]
        ans = max(ans, max(l, r) + (l+r) * (K-1))
        B = [A[i+1] - A[i] for i in range(N-1)]
        B.sort(reverse=True)
        S = 0
        for i, b in enumerate(B, start=1):
            l += b // 2
            r += b // 2
            S += b // 2
            if K-1-i >= 0:
                ans = max(ans, max(l, r) + S + (l+r) * (K-1-i))
            elif K-1-i == -1:
                ans = max(ans, S)
            else:
                break

        print(ans)


if __name__ == "__main__":
    main()
