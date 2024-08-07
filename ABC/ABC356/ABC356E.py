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
    maxa = max(A)
    C = [0] * (10**6+5)
    for a in A:
        C[a] += 1
    cum = list(accumulate([0]+C))
    ans = 0
    for m in range(1, maxa+1):
        for k in range(1, 10**6+1):
            L = m * k
            R = L + m
            if L > maxa:
                break
            R = min(10**6+1, R)
            # print(m, k, L, R)
            if R <= L:
                break
            if k > 1:
                ans += (cum[R]-cum[L]) * k * C[m]
            else:
                ans += (cum[R]-cum[L+1]) * k * C[m] + C[L] * (C[L] - 1) // 2
            # print(ans)
    print(ans)


if __name__ == "__main__":
    main()
