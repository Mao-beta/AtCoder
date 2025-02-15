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
    C = NLI()
    L, R = NMI()

    def f(x):
        return C[0] + C[1]*x + C[2]*x**2 + C[3]*x**3

    import time
    import random
    start = time.time()
    ans = 10**10
    while time.time() - start < 1.9:
        x = random.uniform(L, R)
        ans = min(ans, abs(f(x)))
    print(ans)


if __name__ == "__main__":
    main()
