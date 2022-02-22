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


def s(l, r, k):
    return (l+r) * k // 2


def main():
    T = NI()
    for _ in range(T):
        N, M = NMI()
        XY = [NLI() for _ in range(N)]

        ans = 0
        a = 0
        b = 0
        for x, y in XY:
            if b * x >= 0:
                l = b + x
                r = b + x * y
                k = y
                a += s(l, r, k)
                b = r
                ans = max(a, ans)
                # print(a, b)

            elif b < 0 and x > 0:
                kl = (-b) // x
                if 0 < kl < y:
                    ll = b + x
                    rl = b + x * kl
                    a += s(ll, rl, kl)
                    b = rl

                    ans = max(a, ans)
                    # print(a, b)

                    y -= kl
                    l = b + x
                    r = b + x * y
                    k = y
                    a += s(l, r, k)
                    b = r

                else:
                    l = b + x
                    r = b + x * y
                    k = y
                    a += s(l, r, k)
                    b = r
                    ans = max(a, ans)
                    # print(a, b)


            elif b > 0 and x < 0:
                kl = b // (-x)
                if 0 < kl < y:
                    ll = b + x
                    rl = b + x * kl
                    a += s(ll, rl, kl)
                    b = rl

                    ans = max(a, ans)
                    # print(a, b)

                    y -= kl
                    l = b + x
                    r = b + x * y
                    k = y
                    a += s(l, r, k)
                    b = r

                    ans = max(a, ans)
                    # print(a, b)
                else:
                    l = b + x
                    r = b + x * y
                    k = y
                    a += s(l, r, k)
                    b = r
                    ans = max(a, ans)
                    # print(a, b)

        print(ans)

if __name__ == "__main__":
    main()
