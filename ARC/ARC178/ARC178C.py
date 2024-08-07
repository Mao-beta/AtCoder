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
    N, L = NMI()
    A = NLI()
    INF = 10**10
    dp = [INF] * 200001
    dp[0] = 0
    for k in range(1, L//2+1):
        if k > L-k:
            break
        x = k * (L-k)
        if x > 200000:
            break
        for i in range(200001):
            ni = i + x
            if ni > 200000:
                break
            if dp[ni] <= dp[i] + 1:
                continue
            dp[ni] = dp[i] + 1
    for a in A:
        ans = dp[a]
        print(ans if ans < INF else -1)


if __name__ == "__main__":
    main()
