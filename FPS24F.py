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
    # 指数型母関数
    # (1+y+...)(1+y^2+...)(y+y^3+...) [y^N]
    # e^x * (e^x + e^-x)/2 * (e^x - e^-x)/2 [x^N / N!]
    # 1/4 * (e^3x - e^-x) [x^N / N!]
    # = 1/4 * (3^N - (-1)^N)
    ans = (pow(3, N, MOD99) - (-1) ** (N % 2)) * pow(4, -1, MOD99) % MOD99
    print(ans)


if __name__ == "__main__":
    main()
