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
    N, K = NMI()
    AB = EI(N)
    AB.sort(key=lambda x: (x[0]-1)/x[1])
    dp = [[-1]*(K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        a, b = AB[i]
        for k in range(K+1):
            if dp[i][k] < 0:
                continue
            dp[i+1][k] = max(dp[i+1][k], dp[i][k])
            if k < K:
                dp[i+1][k+1] = max(dp[i+1][k+1], dp[i][k] * a + b)
    print(dp[-1][K])


if __name__ == "__main__":
    main()
