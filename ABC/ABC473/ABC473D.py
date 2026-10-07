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
    N, K = NMI()
    ans = []

    L = []

    def rec(i, rem):
        if i == 1:
            L.append(rem)
            ans.append(L[::-1])
            L.pop()
            return

        for ia in range(0, rem+1, i):
            a = ia // i
            L.append(a)
            rec(i-1, rem-ia)
            L.pop()

    rec(N, K)
    ans.sort()
    for row in ans:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
