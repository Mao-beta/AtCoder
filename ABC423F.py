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
    N, M, Y = NMI()
    A = NLI()
    dp = [0] * (1<<N)
    for b in range(1<<N):
        lcm = 1
        for i in range(N):
            if (b >> i) & 1:
                lcm = math.lcm(lcm, A[i])
            if lcm > Y:
                break
        dp[b] = Y // lcm
    for j in range(N):
        bit = 1 << j
        for i in range(1 << N):
            if i & bit == 0:
                dp[i] -= dp[i | bit]
    ans = 0
    for b in range(1<<N):
        if b.bit_count() == M:
            ans += dp[b]
    print(ans)


if __name__ == "__main__":
    main()
