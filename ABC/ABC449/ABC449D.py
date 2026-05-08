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
    L, R, D, U = NMI()
    ans = 0
    for y in range(D, U+1):
        if y % 2:
            continue
        l = max(L, -abs(y))
        r = min(R, abs(y))
        ans += max(r-l+1, 0)
        # print(y, l, r)
    for x in range(L, R+1):
        if x % 2 or x == 0:
            continue
        l = max(D, -abs(x)+1)
        r = min(U, abs(x)-1)
        ans += max(r-l+1, 0)
        # print(x, l, r)
    print(ans)


if __name__ == "__main__":
    main()
