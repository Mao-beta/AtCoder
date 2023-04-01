import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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
    L, A, B, M = NMI()

    def ar_sum(a, r, n, m):
        """初項a, 公比r, 項数nの等比級数の総和のmod m"""
        res = (pow(r, n, m*(r-1)) - 1) // (r-1) * a % m
        return res

    ans = 0

    for k in range(1, 19):
        l = (10**(k-1) - A + B-1) // B
        r = (10**k - A + B-1) // B - 1
        l = max(l, 0)
        r = min(r, L-1)
        x = r-l+1
        if x <= 0:
            # print(l, r, x)
            continue

        ans *= pow(10, x * k, M)
        ans %= M

        f = A + l * B
        ans += ar_sum(f, 10**k, x, M)
        ans %= M

        MM = (10**k-1)**2 * M
        y = pow(10**k, x, MM) - 1 - x * 10**k + x
        y = y // ((10**k-1) ** 2) % M
        # print(k, l, r, x, ar_sum(f, 10**k, x, M), y)
        ans += y * B
        ans %= M

    print(ans)


if __name__ == "__main__":
    main()
