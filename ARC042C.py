import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    N, P = NMI()
    AB = EI(N)
    AB.sort(reverse=True)
    dp = [-1] * 5101
    dp2 = [-1] * 5101
    dp[0] = 0
    for i in range(N):
        a, b = AB[i]
        for j in range(5101):
            if dp[j] < 0:
                continue
            dp2[j] = max(dp2[j], dp[j])
            if j <= P:
                dp2[j+a] = max(dp2[j+a], dp[j] + b)
        dp, dp2 = dp2, dp
    ans = max(dp)
    print(ans)


if __name__ == "__main__":
    main()
