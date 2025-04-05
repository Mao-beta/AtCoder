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
    R = NI()
    ans = 0
    for x in range(R):
        Y2 = 4*R**2 - (2*x+1)**2
        u2 = math.isqrt(Y2)
        if u2 % 2 == 0:
            u2 -= 1
        u = (u2-1) // 2
        d2 = -u2
        if d2 % 2 == 0:
            d2 += 1
        d = (d2+1) // 2
        if x == 0:
            ans += u-d+1
        else:
            ans += (u-d+1) * 2
    print(ans)


if __name__ == "__main__":
    main()
