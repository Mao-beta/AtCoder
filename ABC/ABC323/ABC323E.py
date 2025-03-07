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
    N, X = NMI()
    T = NLI()
    dp = [0] * (X+1)
    dp[0] = 1
    inv = pow(N, -1, MOD99)

    for i in range(X+1):
        for j, t in enumerate(T):
            if i+t > X:
                continue
            dp[i+t] += dp[i] * inv % MOD99
            dp[i+t] %= MOD99

    print(sum(dp[-T[0]:]) % MOD99 * inv % MOD99)



if __name__ == "__main__":
    main()
