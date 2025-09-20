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
    N, R = NMI()
    L = NLI()
    lzero = -1
    rzero = -1
    for i in range(N):
        if lzero == -1 and L[i] == 0:
            lzero = i
        if L[i] == 0:
            rzero = i
    if lzero == rzero == -1:
        print(0)
        return

    if rzero < R:
        ans = 0
        for i in range(lzero, R):
            if L[i] == 0:
                ans += 1
            else:
                ans += 2
        print(ans)
    elif R <= lzero:
        ans = 0
        for i in range(R, rzero+1):
            if L[i] == 0:
                ans += 1
            else:
                ans += 2
        print(ans)
    else:
        ans = 0
        for i in range(lzero, rzero+1):
            if L[i] == 0:
                ans += 1
            else:
                ans += 2
        print(ans)


if __name__ == "__main__":
    main()
