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
    N, M = NMI()
    ans = 0
    for i in range(62):
        if (M >> i) & 1 == 0:
            continue
        ans += (N>>(i+1)) * pow(2, i, MOD99) % MOD99
        if (N >> i) & 1:
            ans += (N & ((1<<i)-1)) + 1
        ans %= MOD99
    print(ans)


if __name__ == "__main__":
    main()
