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
    x, y = 0, 0
    ans = 0
    for _ in range(N):
        X, Y = NMI()
        ans += math.sqrt((X-x)**2 + (Y-y)**2)
        x, y = X, Y
    ans += math.sqrt(x**2 + y**2)
    print(ans)


if __name__ == "__main__":
    main()