import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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
    # dp[i][b]: i個みて、作れる数の集合が b (0~10の11bit)である確率
    B = 1 << 11
    dp = [[0]*B for _ in range(N+1)]
    dp[0][1] = 1
    for i in range(N):
        a = A[i]
        inv = pow(a, -1, MOD99)
        for b in range(B):
            if dp[i][b] == 0:
                continue
            for x in range(1, 11):
                if x > a:
                    break
                nb = (b | (b << x)) & (B-1)
                dp[i+1][nb] += dp[i][b] * inv % MOD99
                dp[i+1][nb] %= MOD99

            if a > 10:
                dp[i+1][b] += dp[i][b] * inv * (a-10) % MOD99
                dp[i+1][b] %= MOD99

    ans = 0
    for b in range(B):
        if (b >> 10) & 1:
            ans += dp[N][b]
            ans %= MOD99
    print(ans)


if __name__ == "__main__":
    main()
