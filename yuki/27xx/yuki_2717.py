import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    A = NLI()
    ans = 0
    for i, a in enumerate(A):
        tmp = 0
        tmp += pow(2, N-1, MOD99)
        tmp += (N-1) * pow(2, N-2, MOD99)
        tmp += i * (N-1-i) * pow(2, N-3, MOD99)
        ans += tmp * a
        ans %= MOD99
    print(ans)


if __name__ == "__main__":
    main()
