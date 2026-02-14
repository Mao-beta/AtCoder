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
    N, M = NMI()
    F = [NI() for _ in range(N)]
    dp = [0] * (N+1)
    dp[0] = 1
    cum = [0] * (N+2)
    cum[1] = 1
    S = set()
    l = 0
    for i in range(N):
        f = F[i]
        while f in S:
            S.discard(F[l])
            l += 1
        S.add(f)
        # print(f, S, dp, cum)
        dp[i+1] = (cum[i+1] - cum[l]) % MOD
        if dp[i+1] < 0:
            dp[i+1] += MOD
        cum[i+2] = (cum[i+1] + dp[i+1]) % MOD
        if cum[i+2] < 0:
            cum[i+2] += MOD
    # print(dp)
    # print(cum)
    print(dp[-1] % MOD)


if __name__ == "__main__":
    main()
