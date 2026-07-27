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
    T = NI()
    INF = 10**6
    for _ in range(T):
        S = SI()
        N = len(S)
        K = NI()
        dp = [[INF]*(K+1) for _ in range(N+1)]
        dp[0][0] = 0
        for i in range(N):
            for j in range(K+1):
                dp[i+1][j] = min(dp[i+1][j], dp[i][j])
                if i <= N-3:
                    bad = False
                    for k in range(3):
                        if S[i+k:i+k+3] == "ABC":
                            bad = True
                    p = 0
                    for k in range(3):
                        if S[i+k] != "ABC"[k]:
                            p += 1
                    if bad:
                        dp[i+3][j] = min(dp[i+3][j], dp[i][j]+p)
                    elif j < K:
                        dp[i+3][j+1] = min(dp[i+3][j+1], dp[i][j]+p)
        print(*dp, sep="\n")
        print(dp[N][K])


if __name__ == "__main__":
    main()
