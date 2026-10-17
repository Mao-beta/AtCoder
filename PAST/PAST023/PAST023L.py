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
    N, M = NMI()
    AB = EI(N)
    INF = 10**8
    dp = [[-INF]*(2*M+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        a, b = AB[i]
        for j in range(-M, M+1):
            if -M <= j+a <= M:
                dp[i+1][j+a] = max(dp[i+1][j+a], dp[i][j] + a)
            if -M <= j-b <= M:
                dp[i+1][j-b] = max(dp[i+1][j-b], dp[i][j])
    # print(*dp, sep="\n")
    ans = max(dp[N])
    print(ans if ans >= 0 else -1)


if __name__ == "__main__":
    main()
