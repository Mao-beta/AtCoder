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
    V = NLI()
    dp = [[[0, -1] for _ in range(2)] for _ in range(N+1)]
    for i in range(N):
        v = V[i]            
        dp[i+1][0] = dp[i][0][:]
        if dp[i+1][0][0] < dp[i][1][0]:
            dp[i+1][0] = dp[i][1][:]
        dp[i+1][1] = [dp[i][0][0]+v, i]
    # print(*dp, sep="\n")
    if dp[N][0][0] > dp[N][1][0]:
        v, t = dp[N][0]
    else:
        v, t = dp[N][1]
    print(v)
    ans = []
    while t >= 0:
        ans.append(t+1)
        v, t = dp[t][0]
    print(*ans[::-1])


if __name__ == "__main__":
    main()
