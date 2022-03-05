import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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


def main():
    INF = 10 ** 10
    N = NI()
    H = NLI() + [INF] * 5

    dp = [INF] * (N+3)
    dp[0] = 0

    for i in range(N):
        dp[i+1] = min(dp[i+1], dp[i] + abs(H[i] - H[i+1]))
        dp[i+2] = min(dp[i+2], dp[i] + abs(H[i] - H[i+2]))

    print(dp[N-1])


if __name__ == "__main__":
    main()
