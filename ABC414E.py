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
    rN = math.isqrt(N)
    ans = (N+1)*N // 2 # Σ(N-b+1) b=1...N
    ans %= MOD99
    tmp = 0
    for b in range(1, rN+1):
        tmp += N // b
    ans -= tmp * 2 - rN**2
    print(ans % MOD99)


if __name__ == "__main__":
    main()
