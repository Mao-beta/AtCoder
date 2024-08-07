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
    D = NI()
    ans = 10**20
    for x in range(2*10**6):
        if x**2 >= D:
            ans = min(ans, x**2 - D)
            break

        y2 = D - x**2
        l = math.isqrt(y2)
        r = l + 1
        ans = min(ans, abs(x ** 2 + l ** 2 - D))
        ans = min(ans, abs(x ** 2 + r ** 2 - D))
    print(ans)


if __name__ == "__main__":
    main()
